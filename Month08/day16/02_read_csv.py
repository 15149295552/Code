'''
文本文件的读取
'''
import os

import tensorflow as tf


def read_csv(filelist):
    # 构建文件队列
    file_queue = tf.train.string_input_producer(filelist)
    # 定义读取器
    reader = tf.TextLineReader()
    # 使用读取器在文件队列中读取数据
    k, v = reader.read(file_queue)
    # 解码
    records = [['None'], ['None']]
    example, label = tf.decode_csv(v, record_defaults=records)
    # 批处理
    example_bat, label_bat = tf.train.batch([example, label],
                                            batch_size=15,
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
        #开启队列运行的线程
        threads = tf.train.start_queue_runners(sess,coord)
        exam,lab = sess.run([example,label])
        print(exam)
        print(lab)
        #等待线程结束，回收资源
        coord.request_stop()
        coord.join(threads)





