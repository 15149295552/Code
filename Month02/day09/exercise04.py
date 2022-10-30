"""
    内存图训练
"""


class MobilePhone:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

# 练习1
hua_wei = MobilePhone("华为", 7000)
iphone = hua_wei
iphone.brand = "苹果"
print(hua_wei.brand)  # ?

# 练习2
def func01(p1, p2):
    p1.brand = "huawei"
    p2 = MobilePhone("iphone", 8000)

hua_wei = MobilePhone("华为", 7000)
iphone = MobilePhone("苹果", 8000)
func01(hua_wei, iphone)
print(hua_wei.brand)
print(iphone.brand)

# 练习3
hua_wei = MobilePhone("华为", 7000)
list_phone = [
    hua_wei,
    MobilePhone("苹果", 8000)
]
value = 0
for item in list_phone:
    value += item.price
print(value)  # ?
