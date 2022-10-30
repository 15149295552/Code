"""
    异常处理
        适用性:不管语法错误,只针对逻辑错误
        异常现象:程序不再向下执行,而是不断向上返回
        处理:将错误执行流程(上)改为正常执行流程(下)
        价值:保障程序能够按照既定的流程执行,不紊乱
"""


# 语法错误
# print(qtx) # NameError
# print(1 + "1")  # TypeError
# print([10][1]) # IndexError
# print({"a":10}["A"]) # KeyError
# class Wife:
#     pass
#
# shuang_er = Wife()
# print(shuang_er.name) # AttributeError

# 逻辑错误:往往数据超过有效范围引发的错误
# def div_apple(apple_count): # 3
#     # ValueError
#     person_count = int(input("请输入人数："))
#     # ZeroDivisionError
#     result = apple_count / person_count
#     print(f"每人{result}个苹果")
#
# def main():  # 2
#     div_apple(10)
#
# main() # 1


# 语法1:包治百病(民间喜爱)
def div_apple(apple_count):
    try:
        # ValueError
        person_count = int(input("请输入人数："))
        # ZeroDivisionError
        result = apple_count / person_count
        print(f"每人{result}个苹果")
    # except Exception:
    except:
        print("分苹果出错啦")

div_apple(10)
print("后续逻辑")

# 语法2:对症下药(官方建议)
# def div_apple(apple_count):
#     try:
#         # ValueError
#         person_count = int(input("请输入人数："))
#         # ZeroDivisionError
#         result = apple_count / person_count
#         print(f"每人{result}个苹果")
#     except ValueError:
#         print("错误!别输入乱七八糟的")
#     except ZeroDivisionError:
#         print("错误!别输入0呀")
#
# div_apple(10)
# print("后续逻辑")

# 语法3:无论是否发生异常,一定执行的逻辑
# def div_apple(apple_count):
#     try:
#         # ValueError
#         person_count = int(input("请输入人数："))
#         # ZeroDivisionError
#         result = apple_count / person_count
#         print(f"每人{result}个苹果")
#         # 文件处理
#         # 1.打开
#         # 2.处理
#     finally:
#         # 3.关闭
#         print("分苹果结束")
#
# div_apple(10)
# print("后续逻辑")