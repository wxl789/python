import socket
# 1、创建一个socket对象,作为当前项目的服务端使用。
# socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 参数1：指定应用协议：socket.AF_INET 或 socket.AF_INET6 （IPv4， IPv6）
# 参数2：以流的形式发送或接收数据， TCP协议使用流的方式，socket.SOCK_STREAM
socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2、绑定ip地址及端口号
# 注：bind需要的参数为元组类型的参数，
# 元组中的第一个元素为 IP地址。
# 元组中的第二个元素为 端口号。
socketServer.bind(("10.31.160.70", 39999))
# 3、监听
# 在拒绝或断开链接之前的最大连接数量，至少为1。
socketServer.listen(5)
print("服务器已启动，等你链接...")
# 4、等待客户端链接,阻塞程序运行
# accept()：有返回值，可以返回客户端的socket及IP地址
socketClient, addressClient = socketServer.accept()
print(socketClient, addressClient)

while True:
    # 5、接收客户端的数据
    data = socketClient.recv(1024)
    print("客户1%s说%s" % (addressClient, data.decode("utf-8")))
    # 6、发送数据
    sendStr = input("请输入发送的内容：")
    socketClient.send(sendStr.encode("utf-8"))



