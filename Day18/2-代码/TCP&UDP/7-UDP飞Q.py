# 1_lbt4_10#32499#002481627512#0#0#0:1289671407:名字:备注:288:发送的内容

import socket
# 1、创建一个socket对象,作为当前项目的客户端使用。
# socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 参数1：指定应用协议：socket.AF_INET 或 socket.AF_INET6 （IPv4， IPv6）
# 参数2：以包的形式发送或接收数据， UDP协议使用包的方式，socket.SOCK_DGRAM
socketFQ = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
str1 = "1_lbt4_10#32499#002481627512#0#0#0:1289671407:Meakelra:漂亮美眉:288:你好帅，交个朋友好不好"

# 2、发送数据
# sendto(发送的数据,(IP地址, 端口号))
# socketFQ.sendto(str1.encode("gbk"), ("10.31.160.75", 2425))

# 群发
for i in range(256):
    socketFQ.sendto(str1.encode("gbk"), ("10.31.160.%d"%i, 2425))
# 3、关闭链接
socketFQ.close()


