# 异常 exception

# 当程序异常后,后续的语句不会继续向下执行
# L = [1, 4, 5, 6]
# res = L[5]
# print(res)

# def div_apple(count):
#     person_number = int(input('请输入人数:'))
#     result = count / person_number
#     print('每人分得:', result)

# div_apple(10)

# ValueError: invalid literal for int() with base 10: 'a'
# ZeroDivisionError: division by zero

# 异常处理的前提: 语句哪里异常,就在哪里处理
# 目的: 将程序转为正常的执行流程 (异常未知)
# 语法结构1:
# 推荐的处理方法: 异常分类处理
# try:
#     div_apple(10)
# except ValueError:
#     print('输入错误')
# except ZeroDivisionError:
#     print('人数不能为零')
#
# print('函数执行结束')


# try:
#     div_apple(10)
# except (ValueError, ZeroDivisionError):
#     print('输入错误')
#
# print('函数执行结束')


# try:
#     div_apple(10)
# except:  # 所有异常都在此处理 (不太适合异常的进一步优化)
#     print('输入错误')
#
# print('函数执行结束')


# 现实写法(终极写法)
# try:
#     div_apple(10)
# except Exception as e:
#     print('输入错误:', e)


# def div_apple(count):
#     try:
#         # 可能发生异常的语句
#         person_number = int(input('请输入人数:'))
#         result = count / person_number
#         print('每人分得:', result)
#     except Exception as e:
#         # 异常处理的语句
#         print('输入错误', e)
#
# div_apple(10)
# print('函数执行结束')


# # 语法结构2:
# def div_apple(count):
#     try:
#         # 可能发生异常的语句
#         person_number = int(input('请输入人数:'))
#         result = count / person_number
#     except Exception as e:
#         # 异常处理的语句
#         print('输入错误', e)
#     else:
#         # 未发生异常的语句
#         print('每人分得:', result)
#
# div_apple(10)
# print('函数执行结束')


# 语法结构3:
def div_apple(count):
    try:
        # 可能发生异常的语句
        person_number = int(input('请输入人数:'))
        result = count / person_number
    except Exception as e:
        # 异常处理的语句
        print('输入错误', e)
    else:
        # 未发生异常的语句
        print('每人分得:', result)
    finally:
        # 无论是否发生异常,都执行的语句
        print('函数执行结束')

div_apple(10)
