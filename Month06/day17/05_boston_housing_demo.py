# 05_boston_housing_demo.py
# 利用神经网络实现波士顿房价预测
"""
数据集：包含506个样本(102笔用于测试)，13个特征，1个标签
"""
import paddle
import paddle.fluid as fluid
import numpy as np
import os
import matplotlib.pylab as plt

# 第一步：准备数据
BATCH_SIZE = 20 # 批次大小

## reader
reader = paddle.dataset.uci_housing.train() #训练集
rand_reader = paddle.reader.shuffle(reader, 500)#随机reader
train_reader = paddle.batch(rand_reader, BATCH_SIZE)#批量reader

## 打印一个批次数据
# for sample_data in train_reader():
#     print(sample_data)
#     break

# 第二步：定义模型、损失函数、优化器
## 占位符
x = fluid.layers.data(name="x", shape=[13], dtype="float32")
y = fluid.layers.data(name="y", shape=[1], dtype="float32")
## 线性模型(fc)
y_predict = fluid.layers.fc(input=x, # 输入
                            size=1,# 输出值个数(神经元数量)
                            act=None)#回归问题不采用激活函数
## 损失函数
cost = fluid.layers.square_error_cost(input=y_predict,
                                      label=y)
avg_cost = fluid.layers.mean(cost) # 均方差
## 优化器
optimizer = fluid.optimizer.SGD(learning_rate=0.001)
optimizer.minimize(avg_cost)#指定优化的目标函数

## 执行器
place = fluid.CPUPlace()
exe = fluid.Executor(place)
exe.run(fluid.default_startup_program())# 初始化

## feeder(数据喂入器，给模型传入数据)
feeder = fluid.DataFeeder(place=place, # 设备对象
                          feed_list=[x, y])#要喂入的张量

# 第三步：训练，保存模型
iter = 0
iters = [] # 记录迭代次数
train_costs = [] # 记录损失值

for epoch in range(120): # 外层循环控制轮次
    i = 0
    for data in train_reader(): # 内层循环控制批次
        i += 1
        c = exe.run(fluid.default_main_program(),
                    feed=feeder.feed(data), # 喂入的数据
                    fetch_list=[avg_cost])#返回损失函数的值
        if i % 10 == 0:
            print("epoch:%d, cost:%.5f" % (epoch, c[0][0]))
        iter = iter + BATCH_SIZE # 记录批次
        iters.append(iter) # 存入列表
        train_costs.append(c[0][0])#记录损失函数值

# 保存模型
model_save_dir = "model/" # 模型保存的目录
if not os.path.exists(model_save_dir):
    os.makedirs(model_save_dir) # 不存在则创建
# save_inference_model:保存推理模型
fluid.io.save_inference_model(model_save_dir,#保存目录
                              ["x"],#模型推理需要喂入的张量名称
                              [y_predict],#预测结果从哪里获取
                              exe)#执行器
print("模型保存成功.")

# 训练过程可视化
plt.figure("Trainning Cost")
plt.title("Trainning Cost")
plt.xlabel("iter")
plt.xlabel("cost")
plt.plot(iters, train_costs, color="red", label="Cost")
plt.grid() # 网格线
plt.savefig("train.png") # 保存图片
plt.show()

# 第四步：加载模型，预测
infer_exe = fluid.Executor(place) # 专门用于推理的执行器
# 加载模型
# infer_prog:推理program
# feed_vars: 推理需要输入的张量名称列表
# fetch_targets：模型推理结果从这里获取
infer_prog, feed_vars, fetch_targets = \
    fluid.io.load_inference_model(model_save_dir,#模型保存目录
                                  infer_exe)#推理执行器
# 测试集reader
infer_reader = paddle.batch(
    paddle.dataset.uci_housing.test(),#测试集reader
    batch_size=200)

test_data = next(infer_reader()) # 读取一个批次的测试数据
# 取出输入、标签部分
test_x = np.array([data[0] for data in test_data])
test_x = test_x.astype("float32")

test_y = np.array([data[1] for data in test_data])
test_y = test_y.astype("float32")

# 参数字典
params = {feed_vars[0] : test_x} # 预测时只需喂入输入
results = infer_exe.run(infer_prog, # 执行专门推理的program
                        feed=params, # 参数字典
                        fetch_list=fetch_targets)#获取结果

infer_results = [] # 存放预测值
ground_truth = [] # 存放真实值

for val in results[0]: # 取预测值
    infer_results.append(val)

for val in test_y: # 取预测值
    ground_truth.append(val)

# 以真实值作为x,预测值作为y,绘制散点图
plt.figure("Predict & Ground Truth") # 窗体名称
plt.title("Predict & Ground Truth") # 图形名称
plt.xlabel("Ground truth")
plt.ylabel("Infer result")
# 绘制y=x直线
x = np.arange(1, 30) # 在1~30内以步长为1产生一批x值
y = x
plt.plot(x, y) # y=x参照线
# 绘制散点
plt.scatter(ground_truth, infer_results, color="green",
            label="Test")
plt.grid() # 网格线
plt.legend() # 图例
plt.savefig("predict.png") # 保存图片
plt.show()

