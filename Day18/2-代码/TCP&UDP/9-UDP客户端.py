import socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # 发送数据
    sendStr = input("发送的内容：")
    client.sendto(sendStr.encode("utf-8"), ("10.31.160.70", 1999))
    # 接收数据
    data, address = client.recvfrom(1024)
    print("%s说%s" % (address, data.decode("utf-8")))
