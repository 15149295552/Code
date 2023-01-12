"""
    将day08/homewrok/exercise01的汽车信息管理系统的数据改为面向对象版本
    汽车类(品牌/价格/级别)
    主函数、显示菜单函数、选择菜单函数、录入电影函数、显示电影函数、删除电影函数、修改电影函数
"""

from typing import List


class Car:
    def __init__(self, brand="", price=0, rank=""):
        self.brand = brand
        self.price = price
        self.rank = rank


list_car = []  # type:List[Car]


def main():
    """程序主要逻辑"""
    while True:
        display_menu()
        select_menu()


def display_menu():
    """显示菜单"""
    print("请输入1键录入汽车")
    print("请输入2键查看汽车")
    print("请输入3键删除汽车")
    print("请输入4键修改汽车")


def input_car():
    """录入汽车"""
    car = Car()
    car.brand = input("请输入品牌:")
    car.price = int(input("请输入价格:"))
    car.rank = input("请输入级别:")
    list_car.append(car)


def display_cars():
    """显示所有汽车"""
    for item in list_car:
        print("品牌:%s,价格是:%s,级别是%s." % (item.brand, item.price, item.rank))


def delete_car():
    """删除汽车"""
    old = input("请输入品牌:")
    for i in range(len(list_car)):  # 0 1
        if list_car[i].brand == old:
            del list_car[i]
            break  # 删除成功则停止循环


def modify_car():
    """修改汽车"""
    old = input("请输入品牌:")
    for item in list_car:
        if item.brand == old:
            item.brand = input("请输入新品牌:")
            item.price = int(input("请输入新价格:"))
            item.rank = input("请输入新级别:")
            break


def select_menu():
    """选择菜单"""
    number = input("请输入选项：")
    if number == "1":
        input_car()
    elif number == "2":
        display_cars()
    elif number == "3":
        delete_car()
    elif number == "4":
        modify_car()


main()
