# 05_boston_housing_demo.py
# 利用神经网络实现波士顿房价预测

# 第一步：数据准备
import paddle
import paddle.fluid as fluid
import numpy as np
import os
import matplotlib.pyplot as plt

BUF_SIZE = 500
BATCH_SIZE = 20 # 批次大小

# reader
reader = paddle.dataset.uci_housing.train() # 训练集reader
rand_reader = paddle.reader.shuffle(reader, BUF_SIZE)
train_reader = paddle.batch(rand_reader, BATCH_SIZE)

# 打印数据
# for sample in train_reader():
#     print(sample)
#     break

# 第二步：定义模型、损失函数、优化器
## 占位符
x = fluid.layers.data(name="x", shape=[13], dtype="float32")
y = fluid.layers.data(name="y", shape=[1], dtype="float32")

y_predict = fluid.layers.fc(input=x, # 输入
                            size=1, # 输出值个数
                            act=None)# 不采用激活函数
## 损失函数
cost = fluid.layers.square_error_cost(input=y_predict,
                                      label=y)
avg_cost = fluid.layers.mean(cost) # 均方差
## 优化器
optimizer = fluid.optimizer.SGD(learning_rate=0.001)
optimizer.minimize(avg_cost) # 指定优化的目标函数

# 第三步：训练
place = fluid.CPUPlace() # CPU执行
exe = fluid.Executor(place) # 执行器
exe.run(fluid.default_startup_program()) # 初始化
## 数据喂入器，自动生成一个张量字典，送入模型
feeder = fluid.DataFeeder(place=place,
                          feed_list=[x, y])#指定喂入模型的张量

iter = 0
iters = [] # 记录迭代次数
train_costs = [] # 记录损失值

for epoch in range(120): # 外层循环控制轮次
    cst = 0
    i = 0
    for bat_id, data in enumerate(train_reader()): # 内层循环控制批次
        i += 1
        cst = exe.run(fluid.default_main_program(),
                      feed=feeder.feed(data),#喂入的数据
                      fetch_list=[avg_cost])#返回损失函数的值
        if i % 10 == 0: # 每10个批次打印
            print("epoch:%d, batch:%d, cost:%.4f" %
                  (epoch, bat_id, cst[0][0]))
        iter += BATCH_SIZE # 累加
        iters.append(iter) # 记录到列表
        train_costs.append(cst[0][0])#损失值记录到列表

## 训练结束，保存模型
model_save_dir = "./model/" # 模型保存路径
if not os.path.exists(model_save_dir):
    os.makedirs(model_save_dir) # 该目录不存在则创建
fluid.io.save_inference_model(model_save_dir,#保存的目录
                              ["x"], #模型预测时需要传入的参数
                              [y_predict],#预测结果从哪里获取
                              exe) # 执行器
print("模型保存成功.")

## 损失函数可视化
plt.figure("Trainning Cost")
plt.title("Trainning Cost")
plt.xlabel("iters", fontsize=14)
plt.ylabel("cost",  fontsize=14)
plt.plot(iters, train_costs, color="red", label="costs")
plt.grid()
plt.legend()
plt.savefig("train.png") # 保存图片
plt.show()


# 第四步：测试
## 测试集reader
test_reader = paddle.dataset.uci_housing.test()
infer_reader = paddle.batch(test_reader, 200)

infer_exe = fluid.Executor(place) # 专门用于推理的执行器
## 加载模型
## infer_prog：推理program(只包含前向计算)
## feed_vars：使用该模型预测需要喂入的参数列表
## fetch_targets：模型推理结果从哪里获取
infer_prog, feed_vars, fetch_targets = \
    fluid.io.load_inference_model(model_save_dir,#模型目录
                                  infer_exe)#执行器
## 从测试集中读取数据
test_data = next(infer_reader()) # 读取一个批次的测试样本
## 拆分输入、标签部分
## test_x: [102, 13]
## test_y: [102, 1]
test_x = np.array([data[0] for data in test_data])
test_x = test_x.astype("float32") # 转浮点类型
test_y = np.array([data[1] for data in test_data])
test_y = test_y.astype("float32")

params = {feed_vars[0]: test_x} # 参数字典
results = infer_exe.run(infer_prog,#执行推理program
                        feed=params,#参数
                        fetch_list=fetch_targets)#返回值
# print(results)

infer_results = [] # 存放预测值
ground_truths = [] # 存放真实值
# 取出预测值
for val in results[0]:
    infer_results.append(val)
# 取出真实值
for val in test_y:
    ground_truths.append(val)

# 绘图
plt.figure("Infer Results")
plt.title("Infer Results")
plt.xlabel("ground truths")
plt.ylabel("infer results")
x = np.arange(1, 30) # 产生数组
y = x
plt.plot(x, y) # y=x参照线

plt.scatter(ground_truths, infer_results, color="green",
            label="Test Sample")
plt.grid()
plt.legend()
plt.savefig("predict.png")
plt.show()



