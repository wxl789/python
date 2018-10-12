import socket
# 线程
from threading import Thread

# 1、创建socket对象
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2、绑定IP及端口
server.bind(("10.31.160.70", 29999))
# 3、设置监听
server.listen(5)

def chatFunc(client, address):
    # 接收数据
    data = client.recv(1024)
    print("%s说%s" % (address,data.decode("utf-8")))
    # 发送数据
    sendStr = input("发送给%s的内容：" % (address, ))
    client.send(sendStr.encode("utf-8"))
# 4、等待链接
while True:
    client, address = server.accept()
    # print(address)
    # 设置线程，进行数据的发送与接收
    # 创建线程
    threadChat = Thread(target=chatFunc, args=(client, address))
    # 启动线程
    threadChat.start()


