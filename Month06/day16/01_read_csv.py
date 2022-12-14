'''
csv文本文件读取示例
'''
import tensorflow as tf
import os


def read_csv(filelist):
    # 构建文件队列
    file_queue = tf.train.string_input_producer(filelist)
    # 构建文件读取器（文本文件读取器）
    reader = tf.TextLineReader()
    # 读取器从文件队列中读取数据
    file, val = reader.read(file_queue)  # file文件名，val数据
    # 解码（转成张量）
    records = [['None'], ['None']]
    example, label = tf.decode_csv(val, record_defaults=records)
    # 分批次
    example_bat,label_bat = tf.train.batch([example, label],
                                           batch_size=20,
                                           num_threads=1)
    return example_bat,label_bat

if __name__ == '__main__':
    #构建文件列表
    dir_name = '../test_data/'
    file_names = os.listdir(dir_name)
    file_list = []
    for f in file_names:
        file_list.append(os.path.join(dir_name,f))

    example,label = read_csv(file_list)

    #开启Session,执行
    with tf.Session() as sess:
        #线程协调器
        coord = tf.train.Coordinator()
        #开启队列的运行的线程
        threads = tf.train.start_queue_runners(sess,coord=coord)

        exam,lab = sess.run([example,label])
        print('特征:',exam)
        print('类别:',lab)
        # 等待线程停止，并回收资源
        coord.request_stop() #请求停止
        coord.join(threads)


