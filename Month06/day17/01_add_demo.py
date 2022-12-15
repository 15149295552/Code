# 01_add_demo.py
import paddle.fluid as fluid

# 定义两个张量（常量）
x = fluid.layers.fill_constant(shape=[1],#形状
                               dtype="int64",#类型
                               value=5)#值
y = fluid.layers.fill_constant(shape=[1],
                               dtype="int64",
                               value=1)
z = x + y # 执行两个张量相加

# 定义执行器（作用是执行前面定义的op）
place = fluid.CPUPlace() # 指定在CPU上执行
exe = fluid.Executor(place) # 执行器(相当于Session)
result = exe.run(fluid.default_main_program(),
                 fetch_list=[z]) # 指定返回操作z的结果
# result是列表，元素就是fetch_list指定的op的返回值
print(type(result))
print(result)

