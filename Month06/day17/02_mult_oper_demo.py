# 02_mult_oper_demo.py
# 占位符传值，返回多个操作结果
import paddle.fluid as fluid
import numpy

# 定义两个张量(data定的是占位符张量)
x = fluid.layers.data(name="x", shape=[2, 3], dtype="float32")
y = fluid.layers.data(name="y", shape=[2, 3], dtype="float32")

# 定义两个op
x_add_y = fluid.layers.elementwise_add(x, y) # 按元素相加
x_mul_y = fluid.layers.elementwise_mul(x, y) # 按元素相乘

# 执行器
place = fluid.CPUPlace() # 指定在CPU上执行
exe = fluid.Executor(place) # 执行器
exe.run(fluid.default_startup_program()) # 初始化

a = numpy.array([[1, 2, 3], [4, 5, 6]])
b = numpy.array([[1, 1, 1], [2, 2, 2]])
params = {"x" : a, "y" : b} # 给占位符传值（根据名称传值）

outs = exe.run(fluid.default_main_program(),#执行main_program
               feed=params, # 参数字典
               fetch_list=[x_add_y, x_mul_y])#指定返回的结果
print(outs[0]) # 打印fetch_list中指定的第一个操作的返回值
print(outs[1]) # 打印fetch_list中指定的第二个操作的返回值