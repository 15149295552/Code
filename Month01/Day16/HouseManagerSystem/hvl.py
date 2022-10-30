# hvl: house view layer   房源视图层
from hcl import HouseController
from hml import HouseModel
import sys


class HouseView:
    def __init__(self):
        # 表示房源逻辑控制对象
        self.__controller = HouseController()

    def __display_menu(self):
        print('功能提示菜单'.center(15))
        print('-' * 20)
        print(' 1 读取房源数据  ')
        print(' 2 添加房源数据  ')
        print(' 3 显示房源数据  ')
        print(' 4 修改房源数据  ')
        print(' 5 删除房源数据  ')
        print(' 6 查询房源数据  ')
        print(' 7 排序房源数据  ')
        print(' 8 保存房源数据  ')
        print(' 9 退出房源系统  ')
        print('-' * 20)

    def __house_data_check(self, message):
        '''
            检查用户输入的数据是否正确
        :param message: str, 提示信息
        :return: int/float, 正确的数值
        '''
        while True:
            try:
                if message[-3:-1] in ('面积', '总价'):
                    value = float(input(message))
                else:
                    value = int(input(message))

                if value > 0:
                    return value
            except Exception:
                print('提示数值必须大于0或整数')

    def __user_choice(self):
        code = input('请输入对应的功能序号[1~9]: ')
        if code == '1':  # 读取房源数据
            self.__controller.read_house_data_from_csv()
        elif code == '2':  # 添加房源数据
            self.__add_house_data()
        elif code == '3':  # 显示房源数据
            self.__show_house_data(self.__controller.list_houses)
        elif code == '4':  # 修改房源数据
            self.__update_house_data()
        elif code == '5':  # 删除房源数据
            self.__delete_house_data()
        elif code == '6':  # 查询房源数据
            self.__find_house_data()
        elif code == '7':  # 排序房源数据
            self.__sort_house_data()
        elif code == '8':  # 保存房源数据
            self.__controller.save_house_data_to_csv()
        elif code == '9':  # 退出房源系统
            sys.exit('谢谢使用')

    def __add_house_data(self):
        '''
            录入房源数据
        :return: None
        '''
        name = input('请输入房源名称:')
        type = input('请输入房源类型:')
        area = self.__house_data_check('请输入房源面积:')
        tprice = self.__house_data_check('请输入房源总价:')
        uprice = self.__house_data_check('请输入房源单价:')
        house = HouseModel(0, name, type, area, tprice, uprice)
        self.__controller.append_house_data(house)  # 房源对象

    def __show_house_data(self, list_data):
        '''
            显示房源数据
        :param list_data: list, 存放房源对象的列表
        :return: None
        '''
        print('{}{}{}{}{}{}'.format('序号'.center(5),
                                    '名称'.center(20),
                                    '户型'.center(15),
                                    '面积(平米)'.center(15),
                                    '总价(元)'.center(30),
                                    '单价(元)'.center(10)))
        print('-' * 100)
        for house in list_data:
            print('{}{}{}{}{}{}'.format(str(house.id).center(5),
                                        house.name.center(20),
                                        house.type.center(15),
                                        str(house.area).center(15),
                                        str(house.tprice).center(30),
                                        str(house.uprice).center(10)))
        print('-' * 100)

    def __get_house_id(self):
        '''
            获取现存所有房源对象的ID
        :return: list,存储所有房源对象ID的列表
        '''
        # 方法1: 列表推导式
        # return [house.id for house in self.__controller.list_houses]

        # 方法2: map + list
        return list(map(lambda house: house.id, self.__controller.list_houses))

    def __update_house_data(self):
        '''
            更新房源数据
        :return: None
        '''
        # 方式1: 传入所有的字段,构建新的数据
        # id = self.__house_data_check('请输入房源的ID:')
        # # 判断用户输入的id是否存在,做一次校验
        # if id in self.__get_house_id():
        #     name = input('请输入房源名称:')
        #     type = input('请输入房源类型:')
        #     area = self.__house_data_check('请输入房源面积:')
        #     tprice = self.__house_data_check('请输入房源总价:')
        #     uprice = self.__house_data_check('请输入房源单价:')
        #     new_house = HouseModel(id, name, type, area, tprice, uprice)
        #     # 根据Controller类中的方法的返回值,判断是否修改成功
        #     if self.__controller.modify_house_data(new_house):
        #         print('修改成功')
        # else:
        #     print('修改失败')

        # 方式2: 传入部分的字段数据,构建新的数据对象
        id = self.__house_data_check('请输入房源的ID:')
        # 判断用户输入的id是否存在,做一次校验
        list_ids = self.__get_house_id()
        if id in list_ids:
            # 1 查找id(唯一)对应的房源对象
            # (1) 从 所有对象id的列表 中查找到id 的索引值
            id_index = list_ids.index(id)
            # (2) 对应到 self.__controller.list_houses 基于索引值找到对应的房源对象
            house_obj = self.__controller.list_houses[id_index]

            # 2 复制查找到的房源对象(作为携带修改数据对象)
            house_temp = house_obj

            while True:
                # 3 提示菜单(显示修改字段)
                print(' 选择序号,修改对应字段 ')
                print(' 1 名字   2 类型   3 面积   4 总价   5 单价')
                print('-' * 30)

                # 4 用户选择对应的序号
                user_choice = input('请输入对应的序号:')

                # 5 提示用户输入对应的字段值
                if user_choice == '1':
                    name = input('请输入新的名字:')
                    house_temp.name = name
                elif user_choice == '2':
                    type = input('请输入新的类型:')
                    house_temp.type = type
                elif user_choice == '3':
                    area = self.__house_data_check('请输入新的面积:')
                    house_temp.area = area
                elif user_choice == '4':
                    tprice = self.__house_data_check('请输入新的总价:')
                    house_temp.tprice = tprice
                elif user_choice == '5':
                    uprice = self.__house_data_check('请输入新的单价:')
                    house_temp.uprice = uprice
                else:
                    print('输入错误,退出修改')
                    break

            # 6 修改 携带修改数据对象 相关属性的值
            if self.__controller.modify_house_data(house_temp):
                print('修改成功')
        else:
            print('修改失败')

    def __delete_house_data(self):
        '''
            删除对应的房源数据
        :return: None
        '''
        del_id = self.__house_data_check('请输入删除的房源对象ID:')
        if del_id in self.__get_house_id():
            # 1 id存在,则删除对应的房源对象
            if self.__controller.remove_house_data(del_id):
                print('删除成功')
            # 2 修改后续的房源对象id
            for i in range(del_id - 1, len(self.__controller.list_houses)):
                self.__controller.list_houses[i].id -= 1
        else:
            print('删除失败')

    def main(self):
        while True:
            # 1 显示菜单
            self.__display_menu()
            # 2 用户选择
            self.__user_choice()

    def __find_house_data(self):
        '''
            根据条件查询并显示对应的结果
        :return: None
        '''
        while True:
            # 1 打印功能菜单
            print(' 选择对应的序号,实现查询 ')
            print(' 1 名字  2 户型  3 面积  4 总价  5 单价')
            print('-' * 30)
            # 2 用户选择
            code = input('请输入查询对应的序号:')
            # 3 判断实现对应的功能
            if code in tuple('12345'):
                if code == '1':
                    keyword = input('请输入查询关键字:')
                    condition = lambda house, value: value in house.name
                elif code == '2':
                    keyword = input('请输入查询的户型:')
                    condition = lambda house, value: house.type == value
                elif code == '3':
                    keyword = self.__house_data_check('请输入查询的面积:')
                    condition = lambda house, value: house.area > value
                elif code == '4':
                    keyword = self.__house_data_check('请输入查询的总价:')
                    condition = lambda house, value: house.tprice > value
                elif code == '5':
                    keyword = self.__house_data_check('请输入查询的单价:')
                    condition = lambda house, value: house.uprice > value
                list_result = self.__controller.query_house_data(condition, keyword)
                self.__show_house_data(list_result)
            else:
                print('请输入正确的查询序号!!')
                break

    def __sort_house_data(self):
        '''
            根据对应的条件返回查询的结果
        :return: None
        '''
        while True:
            # 1 打印功能菜单
            print(' 选择对应的序号,实现排序 ')
            print(' 1 面积  2 总价  3 单价')
            print('-' * 20)
            # 2 用户选择
            code = input('请输入排序对应的序号:')
            # 3 判断实现对应的功能
            if code in tuple('123'):
                if code == '1':
                    func = lambda house: house.area
                elif code == '2':
                    func = lambda house: house.tprice
                elif code == '3':
                    func = lambda house: house.uprice
                while True:
                    try:
                        sort_flag = int(input('请输入排序方式(0 升序/ 1 降序):'))
                        if sort_flag in (0, 1):
                            list_result = self.__controller.sorted_house_data(func, bool(sort_flag))
                            self.__show_house_data(list_result)
                            break
                        else:
                            print('请输入0或1,实现升序或升序')
                    except Exception:
                        print('输入错误')
                break
            else:
                print('请输入对应功能序号(1~3)')



