# 创建UDP服务器
import socket
# 1、创建socket对象
# socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 参数1：指定应用协议：socket.AF_INET 或 socket.AF_INET6 （IPv4， IPv6）
# 参数2：以包的形式发送或接收数据， UDP协议使用包的方式，socket.SOCK_DGRAM
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 2、绑定IP地址及端口号
# 注：bind需要的参数为元组类型的参数，
# 元组中的第一个元素为 IP地址。
# 元组中的第二个元素为 端口号。
server.bind(("10.31.160.70", 1999))

while True:
    # 3、接收数据
    # recvfrom(1024)：返回客户端的数据及客户端的地址
    # data:为接收的数据
    data, address = server.recvfrom(1024)
    print("%s说%s"%(address, data.decode("utf-8")))
    # 4、发送数据
    # sendto(发送的数据,(IP地址, 端口号))
    dataStr = input("发送的内容：")
    server.sendto(dataStr.encode("utf-8"), address)

