# 两个张量相加
import paddle.fluid as fluid

# 定义两个张量
x = fluid.layers.fill_constant(shape=[1],  # 形状,1维1个元素
                               dtype="int64",  # 类型
                               value=5)  # 值
y = fluid.layers.fill_constant(shape=[1],  # 形状,1维1个元素
                               dtype="int64",  # 类型
                               value=1)  # 值
z = x + y  # 定义z操作，此处并未执行

# 定义执行器
place = fluid.CPUPlace()  # 指定在CPU上执行
exe = fluid.Executor(place)  # 执行器(执行图中的操作)
result = exe.run(
    fluid.default_main_program(),  # 执行默认program，此参数可省略
    fetch_list=[z]) # 指定返回哪些操作的结果
print(result)
