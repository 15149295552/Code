# 04_reader_demo.py
# Reade示例
import paddle


# Paddle官方推荐利用闭包实现
def reader_creator(file_path):  # 外部函数
    def reader():  # 内部函数
        with open(file_path, "r") as f:
            lines = f.readlines()
            for line in lines:
                yield line.replace("\n", "")

    return reader  # 外部函数以内部函数作为返回值


reader = reader_creator("test.txt")
shuffle_reader = paddle.reader.shuffle(reader, 10)  # 随机reader
batch_reader = paddle.batch(shuffle_reader, 3)  # 批量reader

# for data in reader(): #从原始reader中读取
# for data in shuffle_reader(): # 从随机reader中取数据
for data in batch_reader():  # 从批量reader中取数据
    print(data, end="")
