'''
练习4：
    根据心理年龄与实际年龄，打印智商等级。
    智商IQ = 心理年龄MA 除以 实际年龄CA 乘以 100
    
    天才：140以上（包含）
    超常：120-139之间（包含）
    聪慧：110-119之间（包含）
    正常：90-109之间（包含）
    迟钝：80-89之间（包含）
    低能：80以下

分析：
    1 获取心理年龄与实际年龄
    2 计算iq
    3 分类判断
        if iq >= 140: '天才'
        elif 120 <= iq <= 139: '超常'
        elif 110 <= iq <= 119: '聪慧'
        elif 90 <= iq <= 109: '正常'
        elif 80 <= iq <= 89: '迟钝'
        else: '低能'
'''

ma = int(input('请输入心理年龄：'))
ca = int(input('请输入实际年龄：'))

if ma > 0 and ca > 0:   # 数据正确情况
    iq = ma / ca * 100
    print(iq)

    if iq >= 140:   # [140, 正无穷)
        print('天才')
    elif 120 <= iq:  # [120, 139]
        print('超常')
    elif 110 <= iq:  # [110, 119]
        print('聪慧')
    elif 90 <= iq:  # [90, 109]
        print('正常')
    elif 80 <= iq:  # [80, 89]
        print('迟钝')
    else:
        print('低能')
else:   # 数据错误情况
    print('年龄值输入错误')


# 方式3：
ma = int(input('请输入心理年龄：'))
if ma > 0:
    ca = int(input('请输入实际年龄：'))
    if ca > 0:  # 数据正确情况
        iq = ma / ca * 100
        print(iq)

        if iq >= 140:  # [140, 正无穷)
            print('天才')
        elif 120 <= iq:  # [120, 139]
            print('超常')
        elif 110 <= iq:  # [110, 119]
            print('聪慧')
        elif 90 <= iq:  # [90, 109]
            print('正常')
        elif 80 <= iq:  # [80, 89]
            print('迟钝')
        else:
            print('低能')
else:  # 数据错误情况
    print('年龄值输入错误')