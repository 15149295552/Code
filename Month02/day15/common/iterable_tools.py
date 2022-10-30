"""
    可迭代对象工具集
        精通函数式编程
        微软Linq
"""

class IterableHelper:
    """
        集成操作框架
        可迭代对象助手:封装对可迭代对象的常用高阶函数
    """
    # 实例方法:操作实例变量
    # 静态方法:不操作实例成员(实例变量/实例方法)
    @staticmethod
    def find_single(iterable, condition):
        """
            在任意可迭代对象中,根据任意条件查找第一个元素
        :param iterable:可迭代对象
        :param condition:函数类型,搜索条件
        :return:满足条件的第一个元素
        """
        for item in iterable:
            if condition(item):
                return item

    @staticmethod
    def find_all(iterable, condition):
        """
            在任意可迭代对象中,根据任意条件查找所有元素
        :param iterable:可迭代对象
        :param condition:函数类型,搜索条件
        :return:生成器对象,推算满足条件的元素
        """
        for item in iterable:
            if condition(item):
                yield item

    @staticmethod
    def get_count(iterable, condition):
        """
            在任意可迭代对象中,根据任意条件查找数量
        :param iterable:可迭代对象
        :param condition:函数类型,搜索条件
        :return:int类型,满足条件的数量
        """
        count = 0
        for item in iterable:
            if condition(item):
                count += 1
        return count

    @staticmethod
    def select(iterable, condition):
        """

        :param iterable:
        :param condition:
        :return:
        """
        for item in iterable:
            yield condition(item)

    @staticmethod
    def sum(iterable, condition):
        """

        :param iterable:
        :param condition:
        :return:
        """
        sum_value = 0
        for item in iterable:
            sum_value += condition(item)
        return sum_value

    @staticmethod
    def get_max(iterable, condition):
        """

        :param iterable:
        :param condition:
        :return:
        """
        max_value = iterable[0]
        for i in range(1, len(iterable)):
            if condition(max_value) <= condition(iterable[i]):
                max_value = iterable[i]
        return max_value

    @staticmethod
    def delete_all(iterable, condition):
        """

        :param iterable:
        :param condition:
        :return:
        """
        count = 0
        for i in range(len(iterable) - 1, -1, -1):
            if condition(iterable[i]):
                del iterable[i]
                count += 1
        return count

    @staticmethod
    def order_by(iterable, condition):
        """

        :param iterable:
        :param condition:
        :return:
        """
        for r in range(len(iterable) - 1):
            for c in range(r + 1, len(iterable)):
                if condition(iterable[r]) > condition(iterable[c]):
                    iterable[r], iterable[c] = iterable[c], iterable[r]

    @staticmethod
    def is_repeat(iterable,condition):
        """

        :param iterable:
        :param condition:
        :return:
        """
        for r in range(len(iterable) - 1):
            for c in range(r + 1, len(iterable)):
                if condition(iterable[r]) == condition(iterable[c]):
                    return True
        return False
