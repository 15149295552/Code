"""
粘包 问题讨论
"""
from socket import  *

sock = socket()
sock.bind(("0.0.0.0",8880))
sock.listen()

conn,addr = sock.accept()
print("Connect from",addr)


d1 = conn.recv(1024)
print("d1:",d1.decode())
d2 = conn.recv(1024)
print("d2:",d2.decode())
d3 = conn.recv(1024)
print("d3:",d3.decode())

conn.close()
sock.close()

