# 元组 tuple

# 表示
# (元素1, 元素2, ...)

# 创建
# 1 空元组（不可变）
t01 = ()
t01 = tuple()
print(t01, type(t01))

# 2 存储任意类型的元素
t02 = (3, 3.15, None, False, 'python', [1, 3], (4, 6))
print(t02)

# 3 构造函数：tuple(可迭代对象)
t03 = tuple(range(5))
t03 = tuple('java')
t03 = tuple([11, 22, 33, 44])    # list --> tuple
print(t03)

# 4 其他创建形式
t04 = (4,)    # 单个元素的存储方式 --> API接口方法的参数
print(t04, type(t04))

t05 = 'a', 'b'
print(t05, type(t05))

# 数据交换
a, b = 10, 20   # a, b = (10, 20)     # 拆包/解包
print(a, b)

# 定位
t06 = ('java', 'c', 'c++', 'c#', 'html')
print('长度:', len(t06))
print('存在:', '++' not in t06)
print('索引：', t06[2])
print('切片：', t06[-3:])

# 遍历
t06 = ('java', 'c', 'c++', 'c#', 'html')

for tiem in t06:
    print(tiem, end=' ')
print('-' * 50)

for i in range(len(t06)):
    print(i, t06[i])
