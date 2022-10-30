# 实例成员 - 实例方法

# 作用: 表达对象的功能/行为

# 定义类
class Phone:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def listen_music(self):   # 实例方法: 实现对象的功能
        # 访问实例变量
        print(f'{self.brand} {self.color}手机可以听歌')

        # 为对象添加属性 (用的较少)
        self.price = 5999

# 实例化对象
hw = Phone('华为', '黑色')
print('对象的变量字典:', hw.__dict__)

# 调用实例方法
hw.listen_music()

print('对象的变量字典:', hw.__dict__)