# 类 class

# 定义类
class Phone:
    pass

# 实例化对象
p01 = Phone()

# 添加属性
p01.name = '华为'
p01.color = '黑色'

# 访问/查看对象的属性
print(p01.name, p01.color)

# 实例化对象
p02 = Phone()

# print(p02.name, p02.color)    # AttributeError
print(p01, p02)

# 属性的函数
print('判断对象是否有此属性:', hasattr(p01, 'name'))
print('判断对象是否有此属性:', hasattr(p02, 'name'))
print('获取对象的属性值:', getattr(p01, 'name'))
print('获取对象的属性值:', getattr(p02, 'name', None))