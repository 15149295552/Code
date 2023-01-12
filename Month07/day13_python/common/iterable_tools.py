"""
    在common/iterable_tools模块中
    可迭代对象工具集
"""


class IterableHelper:
    """
        可迭代对象助手：定义对可迭代对象的各种高阶函数
    """

    @staticmethod  # 静态方法：python解释器不会征收第一个参数self
    def first(iterable, condition):
        """
            在可迭代对象中查找第一个满足条件的元素
        :param iterable: 可迭代对象
        :param condition: 函数类型的查找条件
        :return:第一个满足条件的元素
        """
        for item in iterable:
            if condition(item):
                return item

    @staticmethod
    def last(iterable, condition):
        """
            根据任意条件在任意可迭代对象中查找满足条件的最后一个元素
        :param iterable:
        :param condition:
        :return:
        """
        for i in range(len(iterable) - 1, -1, -1):
            if condition(iterable[i]):
                return iterable[i]

    @staticmethod
    def find_all(iterable, condition):
        """
            在可迭代对象中查找所有满足条件的元素
        :param iterable: 可迭代对象
        :param condition: 函数类型的查找条件
        :return:列表类型,所有满足条件的元素
        """
        list_result = []
        for item in iterable:
            if condition(item):
                list_result.append(item)
        return list_result

    @staticmethod
    def select(iterable, condition):
        """
            在任意可迭代对象中根据任意条件选择元素的成员
        :param iterable:可迭代对象
        :param condition:函数类型的条件
        :return:列表
        """
        list_result = []
        for item in iterable:
            list_result.append(condition(item))
        return list_result

    @staticmethod
    def sum(iterable, condition):
        """
            根据任意条件对可迭代对象中的元素累加
        :param iterable: 可迭代对象
        :param condition: 函数类型的条件
        :return: 累加结果
        """
        value = 0
        for item in iterable:
            value += condition(item)
        return value

    @staticmethod
    def delete_all(iterable, condition):
        """
            根据任意条件在可迭代对象中删除所有满足条件的元素
        :param iterable: 可迭代对象
        :param condition: 函数类型,删除条件
        :return: int类型,删除的元素数
        """
        count = 0
        for i in range(len(iterable) - 1, -1, -1):
            if condition(iterable[i]):
                del iterable[i]
                count += 1
        return count

    @staticmethod
    def get_max(iterable, condition):
        """
            在可迭代对象中,根据任意条件获取最大的元素
        :param iterable: 可迭代对象
        :param condition:函数类型,搜索条件
        :return: 最大的元素
        """
        max_value = iterable[0]
        for i in range(1, len(iterable)):
            if condition(max_value) < condition(iterable[i]):
                max_value = iterable[i]
        return max_value

    @staticmethod
    def get_min(iterable, condition):
        """
            在可迭代对象中,根据任意条件获取最小的元素
        :param iterable: 可迭代对象
        :param condition:函数类型,搜索条件
        :return: 最小的元素
        """
        max_value = iterable[0]
        for i in range(1, len(iterable)):
            if condition(max_value) > condition(iterable[i]):
                max_value = iterable[i]
        return max_value
