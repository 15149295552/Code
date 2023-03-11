'''
图像文件读取示例
'''
import tensorflow as tf
import os


def read_img(file_list):
    # 构建文件队列
    file_queue = tf.train.string_input_producer(file_list)
    # 定义读取器
    reader = tf.WholeFileReader()
    # 读取数据
    k, v = reader.read(file_queue)
    # 解码
    img = tf.image.decode_jpeg(v)
    # 批处理
    resized_img = tf.image.resize(img, (250, 250))
    resized_img.set_shape([250, 250, 3])
    batch_img = tf.train.batch([resized_img],
                               batch_size=10,
                               num_threads=1)
    return batch_img

if __name__ == '__main__':
    #构建文件列表
    dir_names = '../test_img/'
    file_names = os.listdir(dir_names)
    file_list = []
    for f in file_names:
        file_list.append(os.path.join(dir_names,f))

    imgs = read_img(file_list)

    with tf.Session() as sess:
        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(sess,coord)
        img = sess.run(imgs)
        # print(img) #(10,250,250,3)
        coord.request_stop()
        coord.join(threads)

#显示图像
import matplotlib.pyplot as plt

fig = plt.figure('ImgShow',facecolor='lightgray')

for i in range(10):
    plt.subplot(2,5,i+1)
    plt.imshow(img[i].astype('int32'))
    plt.xticks([])
    plt.yticks([])

plt.tight_layout()
plt.show()










