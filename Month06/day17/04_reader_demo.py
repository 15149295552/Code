# 04_reader_demo.py
# reader demo
import paddle

def reader_creator(file_path):
    def reader():
        with open(file_path, "r") as f:
            lines = f.readlines()
            for line in lines:
                yield line.replace("\n", "")
    return reader

reader = reader_creator("test.txt")
shuffle_reader = paddle.reader.shuffle(reader,10)
batch_reader = paddle.batch(shuffle_reader, 3)
# for data in reader():
# for data in shuffle_reader(): # random reader
for data in batch_reader(): # batch reader
    print(data, end="")