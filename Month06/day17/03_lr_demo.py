# 03_lr_demo.py
import paddle
import paddle.fluid as fluid
import numpy as np
import matplotlib.pyplot as plt
# 样本
train_data = np.array([[0.5],
                       [0.6],
                       [0.8],
                       [1.1],
                       [1.4]]).astype('float32')
y_true = np.array([[5.0],
                   [5.5],
                   [6.0],
                   [6.8],
                   [6.8]]).astype('float32')

# 占位符
x = fluid.layers.data(name="x", shape=[1], dtype="float32")
y = fluid.layers.data(name="y", shape=[1], dtype="float32")
# 线性模型
y_predict = fluid.layers.fc(input=x, # 输入
                            size=1,# 神经元数量(输出值个数)
                            act=None)# 回归问题不采用激活函数
# 损失函数
cost = fluid.layers.square_error_cost(input=y_predict,#预测值
                                      label=y)#真实值
avg_cost = fluid.layers.mean(cost) # 均方差
# 优化器
optimizer = fluid.optimizer.SGD(learning_rate=0.01)
optimizer.minimize(avg_cost) # 指定优化的目标函数

# 执行器
place = fluid.CPUPlace() # 在CPU上执行
exe = fluid.Executor(place)
exe.run(fluid.default_startup_program()) # 初始化

params = {"x":train_data, "y":y_true} # 参数字典

costs = [] # 记录损失值
iters = [] # 记录迭代次数

for i in range(100):
    outs = exe.run(fluid.default_main_program(),
                   feed=params,
                   fetch_list=[y_predict, avg_cost])
    print("i:", i, " cost:", outs[1][0])
    iters.append(i) # 记录迭代次数
    costs.append(outs[1][0])

# 线性模型可视化
tmp = np.random.rand(10, 1)  # 生成10行1列的均匀随机数组
tmp = tmp * 2  # 范围放大到0~2之间
tmp.sort(axis=0)  # 排序
x_test = np.array(tmp).astype("float32")
params = {"x": x_test, "y": x_test}  # y参数不参加计算，只需传一个参数避免报错
y_out = exe.run(feed=params,
                fetch_list=[y_predict])  # 预测
y_test = y_out[0]

# 损失函数可视化
plt.figure("Trainging")
plt.title("Training Cost", fontsize=24)
plt.xlabel("Iter", fontsize=14)
plt.ylabel("Cost", fontsize=14)
plt.plot(iters, costs, color="red", label="Training Cost")  # 绘制损失函数曲线
plt.grid()  # 绘制网格线
plt.savefig("train.png")  # 保存图片

# 线性模型可视化
plt.figure("Inference")
plt.title("Linear Regression", fontsize=24)
plt.plot(x_test, y_test, color="red", label="inference")  # 绘制模型线条
plt.scatter(train_data, y_true)  # 原始样本散点图

plt.legend()
plt.grid()  # 绘制网格线
plt.savefig("infer.png")  # 保存图片
plt.show()  # 显示图片