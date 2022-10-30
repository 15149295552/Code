# 内置方法

class Phone:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def __str__(self):  # 将对象转为字符串,在打印对象时被自动调用
        return f'{self.brand}的价格是:{self.price}'


p01 = Phone('华为', 6999)
print(p01)    # <__main__.Phone object at 0x0000021B4CECA7C0>
print(p01.price, p01.brand)

list_phone = [
    Phone('华为', 6999),
    Phone('小米', 5999),
    Phone('VIVO', 4999),
    Phone('1+', 6000),
    Phone('OPPO', 1888)
]

for phone in list_phone:
    if phone.price > 5000:
        print(phone)