"""
粘包 问题讨论
"""
from socket import *
from time import sleep

sock = socket()
sock.connect(("127.0.0.1",8880))

# 增加延迟，等第一个内容被接收再发第二个
# sock.send(b"aaaa")
# sleep(0.2)
# sock.send(b"bbbb")
# sleep(0.2)
# sock.send(b"cccc")

# 增加格式控制  让对方能够区分出每个消息
sock.send(b"aaaa/")
sock.send(b"bbbb/")
sock.send(b"cccc/")


sock.close()

