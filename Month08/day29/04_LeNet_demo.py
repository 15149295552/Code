# 04_LeNet_demo.py
# 实现LeNet模型
import torch
import torch.nn as nn
import torchvision
import torch.optim as optim
import torch.nn.functional as F
import torchvision.transforms as transforms
import os


class LeNet(nn.Module):
    def __init__(self):
        super(LeNet, self).__init__()

        self.conv_block = nn.Sequential(
            nn.Conv2d(3, 16, 5),  # 输入3通道, 输出16通道28*28, 卷积核5*5
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2, 2),  # 输出：16通道, 14*14

            nn.Conv2d(16, 32, 5),  # 输入16通道,输出32通道,卷积核5*5
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2, 2),  # 输出：32通道, 5*5
        )

        self.classifier = nn.Sequential(
            nn.Linear(32 * 5 * 5, 120),  # 第一层fc
            nn.ReLU(inplace=True),
            nn.Linear(120, 84),  # 第二层fc
            nn.ReLU(inplace=True),
            nn.Linear(84, 10)  # 第三层fc
        )

    def forward(self, x):
        features = self.conv_block(x)  # 卷积池化部分
        flat_features = torch.flatten(features, start_dim=1)
        out = torch.nn.Softmax(dim=1)(self.classifier(flat_features))

        return out


def main():
    model_path = "./Lenet.pth"  # 模型文件路径
    # 定义图像预处理操作(图像数据会按照以下顺序进行预处理)
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])

    # 训练集reader和batch reader
    train_set = torchvision.datasets.CIFAR10(
        root="./",  # 数据集路径(当前目录)
        train=True,  # 训练集
        download=True,  # 没有找到文件是否下载
        transform=transform)  # 预处理步骤
    train_loader = torch.utils.data.DataLoader(
        train_set,  # 指定reader
        batch_size=36,  # 批次大小
        shuffle=True,  # 是否做随机化处理
        num_workers=0)  # 进程数量(0表只使用主进程)

    # 评估集
    val_set = torchvision.datasets.CIFAR10(root="./",
                                           train=False,
                                           download=True,
                                           transform=transform)
    val_loader = torch.utils.data.DataLoader(val_set,
                                             batch_size=5000,
                                             shuffle=False,
                                             num_workers=0)
    val_data_iter = iter(val_loader)  # 迭代器
    val_image, val_label = next(val_data_iter)  # 取出所有评估集数据

    net = LeNet()  # 实例化模型对象

    # 如果模型文件存在，则加载
    if os.path.exists(model_path):
        net.load_state_dict(torch.load(model_path))  # 加载模型参数
        print("加载模型成功.")

    loss_func = nn.CrossEntropyLoss()  # 交叉熵对象
    optimizer = optim.Adam(net.parameters(), lr=0.0001)  # 优化器

    # 开始训练
    for epoch in range(5):
        running_loss = 0.0
        for step, data in enumerate(train_loader):
            inputs, labels = data  # 取出输入、标签部分
            optimizer.zero_grad()

            outputs = net(inputs)  # 正向计算

            loss = loss_func(outputs, labels)  # 计算损失
            loss.backward()  # 反向传播
            optimizer.step()  # 更新参数

            running_loss += loss.item()  # 损失值累加
            if step % 500 == 499:
                with torch.no_grad():  # 关闭梯度做评估
                    outputs = net(val_image)  # 评估集预测
                    pred_y = torch.max(outputs, dim=1)[1]
                    accuracy = torch.eq(pred_y, val_label).sum().item() / val_label.size(0)
                    # 打印
                    print('[%d, %5d] train_loss: %.3f  test_accuracy: %.3f' %
                          (epoch + 1, step + 1, running_loss / 500, accuracy))
                    running_loss = 0.0  # 临时遍历清零
    print('训练结束.')

    torch.save(net.state_dict(), model_path)  # 保存模型


if __name__ == "__main__":
    main()
