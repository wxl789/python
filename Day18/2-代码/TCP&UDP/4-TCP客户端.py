import socket
# 1、创建socket对象
socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2、建立连接
socketClient.connect(("10.31.160.70", 29999))
while True:
    # 3、发送数据
    sendStr = input("请输入发给服务器的数据：")
    socketClient.send(sendStr.encode("utf-8"))
    # 4、接收数据
    data = socketClient.recv(1024)
    print(data.decode("utf-8"))

