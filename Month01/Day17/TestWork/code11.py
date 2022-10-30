'''
11、神奇的数字和
    定义函数：按照格式：s = a + aa + aaa + aaaa + a…a，a表示一个数字，s表示数字计算的和。
        输入：3   5
        输出：37035     # 3 + 33 + 333 + 3333 + 33333

分析:
   1 定义函数: magic_number_sum(number, count)
   2 判断 number != 0
      1 定义变量,记录和, 初始值: number
      2 定义变量(temp),记录number
      2 循环: range(count-1)
         number = number * 10 + temp
         变量 += number
      3 打印结果
'''


def magic_number_sum(number, count):
    '''
        神奇的数字和
    :param number: int, 位上的数
    :param count: int, 个数
    :return: int, 计算的和
    '''
    # 方法1:
    # if number != 0:
    #     sums = number
    #     temp = number
    #     for i in range(count - 1):
    #         number = number * 10 + temp
    #         sums += number
    #     return sums

    # 方法2: 字符串
    # if number != 0:
    #     sums = 0
    #     for i in range(1, count+1):
    #         sums += int(str(number) * i)
    #     return sums

    # 方法3: 列表
    # if number != 0:
    #     list_data = []
    #     for i in range(1, count+1):
    #         num = int(str(number) * i)
    #         list_data.append(num)
    #     print(list_data)
    #     return sum(list_data)

    # 方法4: 字符串拼接 + eval函数
    if number != 0:
        string = ''
        for i in range(1, count + 1):
            num = str(number) * i
            string += num
            if i != count:
                string += '+'
            print(string)
        return eval(string)

print(magic_number_sum(3, 5))