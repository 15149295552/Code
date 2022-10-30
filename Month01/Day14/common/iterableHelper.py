class IterableHelper:
    @staticmethod
    def find(list_employees, condition, value):
        '''
            查找可迭代对象中满足条件的单个数据对象
        :param list_employees: list,存储数据对象的可迭代对象
        :param condition: function, 条件函数
        :param value: any, 值
        :return: object, 满足条件的单个数据对象
        '''
        for emp in list_employees:
            if condition(emp, value):
                return emp

    @staticmethod
    def count(list_employees, condition, value):
        '''
            查找可迭代对象中满足条件的数据对象数量
        :param list_employees: list,存储数据对象的可迭代对象
        :param condition: function, 条件函数
        :param value: any, 值
        :return: int, 满足条件的数据对象个数
        '''
        number = 0
        for emp in list_employees:
            if condition(emp, value):
                number += 1
        return number

    @staticmethod
    def max(list_employees, condition):
        '''
            查找可迭代对象中满足条件的数据对象
        :param list_employees: list,存储数据对象的可迭代对象
        :param condition: function, 条件函数
        :return: object, 满足条件的数据对象
        '''
        # 假设法
        max_employee = list_employees[0]
        for i in range(1, len(list_employees)):
            if condition(list_employees[i]) > condition(max_employee):
                max_employee = list_employees[i]
        return max_employee