# 实例成员 - 实例变量(实例属性)

# 问题: 无论实例化出来多个对象,每个对象都需要拥有 品牌/颜色 (手机对象的属性[特征])
# 措施: 构造方法

# 定义类
class Phone:
    # 在类中的方法本质:
    #   就是函数 [区别：方法中第1个参数默认为self,实例化时不用传参]
    #            相同点: 在方法定义或被调用时,可以参考函数的形参/实参的定义或传参方式
    # 初始化方法/构造方法: 多用于初始化实例对象的属性(变量)
    # self: 自身, 表示实例对象本身
    def __init__(self, brand, color):
        # 定义[实例变量]: 为了实例对象添加属性
        # print(self)
        self.brand = brand
        self.color = color

# 实例化对象
# 在实例化时会自动调用[构造方法], 除了self以外,需要传递对应的数据
hw = Phone('华为', '黑色')
print(hw)

# 访问对象的属性
print(hw.brand, hw.color)

# 查看对象的[变量字典]
print(hw.__dict__)
print(str.__dict__)

# 修改对象的属性值
hw.color = '红色'
print(hw.brand, hw.color)

mi = Phone('小米', '蓝色')
print(mi.brand, mi.color)

vo = Phone('VIVO', '橙色')
print(vo.brand, vo.color)