# 02_mult_op_demo.py
# 执行多个操作，并向模型传参
import paddle.fluid as fluid
import numpy

# layers.data定义占位符(空张量)
x = fluid.layers.data(name="x", shape=[2,3], dtype="float32")
y = fluid.layers.data(name="y", shape=[2,3], dtype="float32")

x_add_y = fluid.layers.elementwise_add(x, y)#按元素相加
x_mul_y = fluid.layers.elementwise_mul(x, y)#按元素相乘

place = fluid.CPUPlace() # 在CPU上执行
exe = fluid.Executor(place)#执行器
exe.run(fluid.default_startup_program()) # 初始化

# 占位符传值
a = numpy.array([[1, 2, 3], [4, 5, 6]])
b = numpy.array([[1, 1, 1], [2, 2, 2]])
params = {"x":a, "y":b}  # 参数字典

outs = exe.run(fluid.default_main_program(),
               feed=params, # 参数字典
               fetch_list=[x_add_y, x_mul_y])#返回两个操作计算结果
print(outs[0]) # 取出第一个操作(x_add_y)的结果
print(outs[1]) # 取出第二个操作(x_mul_y)的结果

