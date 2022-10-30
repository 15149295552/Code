# hcl: house controller layer  房源逻辑控制层
import csv
from hml import HouseModel


class HouseController:
    # 初始房源ID
    init_id = 0

    def __init__(self):
        self.__list_houses = []  # 存储所有的房源对象(只读模式)

    @property
    def list_houses(self):  # 读取方法
        return self.__list_houses

    def read_house_data_from_csv(self):
        '''
            从csv文件中读取房源数据
        :return: None
        '''
        self.__list_houses.clear()
        f = open('./house.csv', 'r', encoding='gbk')
        csv_reader = csv.reader(f)
        index = 0
        for line in csv_reader:
            list_new_houses = []  # 临时存储处理数据
            if index != 0:
                list_new_houses.extend(line[1:3])
                list_new_houses.insert(0, int(line[0]))
                list_new_houses.extend([eval(d) for d in line[-3:]])
                house_obj = HouseModel(*list_new_houses)
                self.__list_houses.append(house_obj)
            index += 1
        f.close()
        print(f'{len(self.__list_houses)}条房源数据读取成功!!!')

    def append_house_data(self, new_house):
        '''
            添加房源对象
        :param new_house: object, 要添加的房源对象
        :return: None
        '''
        # 1 实现房源id的自增长
        self.__generate_id(new_house, self)

        # 2 添加房源对象到存储的房源对象列表中
        self.__list_houses.append(new_house)

    @classmethod
    def __generate_id(cls, new_house, obj):
        '''
            系统自生成id
        :param new_house: object,添加的房源对象
        :param obj: object, HouseController类实例化对象(通过该对象访问 __list_houses)
        :return: None
        '''
        # 计算存储房源对象列表的长度是否大于0,大于0,获取列表中最后一个房源对象的id,否则设置为0
        cls.init_id = obj.__list_houses[-1].id if len(obj.__list_houses) > 0 else 0
        # 实现类变量init_id 加一
        cls.init_id += 1
        # 修改添加房源的对象的id值
        new_house.id = cls.init_id

    def remove_house_data(self, del_id):
        '''
            根据传入的删除id,从存储房源列表中删除对应的房源对象
        :param del_id: int, 删除的房源id
        :return: bool,删除成功,返回True,否则返回False
        '''
        # 遍历每个房源对象
        for house in self.__list_houses:
            # 比较房源对象的id是否与删除的房源id相等,相等则删除,并且返回True
            if house.id == del_id:
                self.__list_houses.remove(house)
                return True
        return False

    def modify_house_data(self, new_house):
        '''
            根据传入携带房源数据的房源id对比修改列表中存储的房源对象
        :param new_house: object, 携带房源数据的房源对象
        :return: bool,修改成功则返回True,否则返回False
        '''
        # 遍历每个房源对象
        for house in self.__list_houses:
            # 如果id相同,则将携带房源对象的属性值赋值给列表中存储的房源对象对应的属性,并且返回True
            if house.id == new_house.id:
                house.name = new_house.name
                house.type = new_house.type
                house.area = new_house.area
                house.uprice = new_house.uprice
                house.tprice = new_house.tprice
                return True
        return False

    def query_house_data(self, condition, value):
        '''
            根据不同的条件返回查询的所有结果
        :param condition: function, 查询的条件函数
        :param value: any, 查询的数据
        :return: list, 存储满足条件的房源对象
        '''
        list_result = []
        for house in self.__list_houses:
            if condition(house, value):
                list_result.append(house)
        return list_result

    def sorted_house_data(self, func, flag):
        '''
            根据函数及排序方式对数据进行排序
        :param func: function, 排序定义的函数
        :param flag: bool, 升序或降序
        :return: None
        '''
        # 1 自定义: 冒泡排序
        # for i in range(len(self.__list_houses)-1):
        #     for j in range(i+1, len(self.__list_houses)):
        #         if self.__list_houses[i].area < self.__list_houses[j].area:
        #             self.__list_houses[i], self.__list_houses[j] = self.__list_houses[j], self.__list_houses[i]

        # 2 list.sort(key=function, reverse=False)
        # self.__list_houses.sort(key=func, reverse=flag)

        # 3 sorted(iterable, key=function, reverse=False)
        return sorted(self.__list_houses, key=func, reverse=flag)

    def save_house_data_to_csv(self):
        '''
            将存储的房源对象列表数据存储到csv文件中
        :return: None
        '''
        f = open('house.csv', 'w', newline='')
        writer = csv.writer(f)
        for house in self.__list_houses:
            # 方法1:
            # writer.writerow([house.id, house.name, house.type, house.area, house.tprice, house.uprice])

            # 方法2:
            data = list(house.__dict__.values())
            writer.writerow(data)
        f.close()
        print(f'{len(self.__list_houses)}条房源数据保存成功!!!')


if __name__ == '__main__':
    controller = HouseController()
    controller.read_house_data_from_csv()
    controller.read_house_data_from_csv()
    print(len(controller.list_houses))

    # 测试添加房源对象
    # house01 = HouseModel(0, '达内教育大厦', '9层楼', 500, 2000, 72000)
    # controller.append_house_data(house01)

    # 测试删除房源对象
    print(controller.remove_house_data(49))
    print(controller.remove_house_data(100))

    # 测试修改房源对象
    house02 = HouseModel(10, '达内教育大厦', '9层楼', 500, 5000, 62000)
    print(controller.modify_house_data(house02))
    house03 = HouseModel(60, '达内教育大厦', '9层楼', 500, 2000, 52000)
    print(controller.modify_house_data(house03))

    # 测试查询房源数据
    # def condition(house, value):
    #     return value in house.name

    # list_result = controller.query_house_data(lambda house, value: value in house.name,
    #                                           '家')

    # list_result = controller.query_house_data(lambda house, value: house.tprice > value,
    #                                           20000000)

    # list_result = controller.query_house_data(lambda house, value: house.type == value,
    #                                           '3室2厅')

    # 测试排序
    # controller.sorted_house_data()
    # controller.sorted_house_data(lambda house: house.uprice, True)
    # controller.sorted_house_data(lambda house: house.area, False)

    list_result = controller.sorted_house_data(lambda house: house.tprice, True)

    # for h in controller.list_houses:
    # for h in list_result:
    #     print(h)

    # 测试数据保存到csv文件中
    controller.save_house_data_to_csv()
