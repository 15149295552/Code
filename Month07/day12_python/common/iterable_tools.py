"""
    在common/iterable_tools模块中
    可迭代对象工具集
"""
class IterableHelper:
    """
        可迭代对象助手：定义对可迭代对象的各种高阶函数
    """
    @staticmethod # 静态方法：python解释器不会征收第一个参数self
    def first(iterable,condition):
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
    def find_all(iterable,condition):
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

