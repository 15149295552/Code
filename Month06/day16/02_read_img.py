'''
图像读取示例
'''
import tensorflow as tf
import os
import matplotlib.pyplot as plt


def read_img(filelist):
    # 构建文件队列
    file_queue = tf.train.string_input_producer(filelist)
    # 构建全文件读取器
    reader = tf.WholeFileReader()
    # 使用读取器在文件队列中读取数据
    file, val = reader.read(file_queue)
    # 解码
    img = tf.image.decode_jpeg(val)
    # 批处理(每张图像大小必须一致)
    img_resized = tf.image.resize(img, [250, 250])  # 将图片设为250*250
    img_resized.set_shape([250, 250, 3])

    img_bat = tf.train.batch([img_resized],
                             batch_size=10,
                             num_threads=1)

    return img_bat


if __name__ == '__main__':
    #构建文件列表
    dir_name = '../test_img/'
    file_names = os.listdir(dir_name)
    file_list = []
    for f in file_names:
        file_list.append(os.path.join(dir_name,f))

    imgs = read_img(file_list)

    with tf.Session() as sess:
        coords = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(sess,coord=coords)
        result = sess.run(imgs)
        # print(result)
        #等待线程结束，回收资源
        coords.request_stop()
        coords.join(threads)

#显示图像
plt.figure('Img show',facecolor='lightgray')

for i in range(10):
    plt.subplot(2,5,i+1)
    plt.imshow(result[i].astype('int32'))
    plt.xticks([])
    plt.yticks([])

plt.tight_layout()
plt.show()

# 独热编码
# 0:[1 0 0 0 0 0 0 0 0 0]
# 1:[0 1 0 0 0 0 0 0 0 0]
# 2:[0 0 1 0 0 0 0 0 0 0]
# 3:[0 0 0 1 0 0 0 0 0 0]
# 4:[0 0 0 0 1 0 0 0 0 0]
# 5:[0 0 0 0 0 1 0 0 0 0]
# 6:[0 0 0 0 0 0 1 0 0 0]
# 7:[0 0 0 0 0 0 0 1 0 0]
# 8:[0 0 0 0 0 0 0 0 1 0]
# 9:[0 0 0 0 0 0 0 0 0 1]
#


# y:    [0     0    0    0    0    0    0    0    0     1]
# pred_y[0.01 0.01 0.01 0.01 0.01 0.01 0.01 0.01 0.01  0.91]
#
# tf.argmax(y,1)
# tf.argmax(pred_y,1)
# 如果相等，预测对了










