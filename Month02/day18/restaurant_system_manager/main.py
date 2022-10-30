"""
    餐厅信息管理系统restaurant_system_manager
    练习1:搭建MVC架构
        View:显示菜单、选择菜单、1键录入餐厅信息(北京/星期五餐厅/2847/180)
        Model:city、name、remark、money
        Controller:添加餐厅信息

    练习2:添加餐厅信息
        Model:rid
        Controller:添加餐厅信息(加到列表,设置编号)

    练习3:显示所有餐厅信息
        View:输入2键,打印所有餐厅信息

    练习4:删除餐厅信息
        View:输入3键,获取编号传递给controller再判断成败
        controller:循环列表,删除元素

    练习4:修改餐厅信息
        View:输入4键,获取信息传递给controller再判断成败
        controller:循环列表,修改信息

    练习5:封装餐厅信息管理系统
        View:只提供main
        controller:隐藏start_id

    练习6:重构餐厅信息管理系统
        View:直接打印餐厅,重写Model的__str__
        Controller:使用remove移除,重写Model的__eq__

    练习7:将MVC拆分为4个模块

    练习8:在View中进行异常处理
        将所有int(input())代码给为__get_number函数

    练习9:持久化处理
        创建数据访问对象,负责保存/加载数据(文件)
        在控制器中使用
"""
from usl import RestaurantView

if __name__ == '__main__':
    view = RestaurantView()
    view.main()
