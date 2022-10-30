"""
    多个函数名称不能相同
"""
def attack_single():# 4  6
    print("直拳")
    print("摆拳")
    print("勾拳")

def attack_repeat(count): # 2
    for item in range(count):
        attack_single() # 3  5

attack_repeat(2) #1