# 需要使用tcp/udp，需要导入socket套接字的模块
# socket用于网络协议
'''
服务器端：接收客户端的数据，给客户端发送数据
客户端：向服务器发送请求，接收服务器的数据。
'''
import socket
# 1、创建一个socket对象,作为当前项目的客户端使用。
# socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 参数1：指定应用协议：socket.AF_INET 或 socket.AF_INET6 （IPv4， IPv6）
# 参数2：以流的形式发送或接收数据， TCP协议使用流的方式，socket.SOCK_STREAM
socketXL = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2、建立TCP链接
# 注：connect需要的参数为元组类型的参数，
# 元组中的第一个元素为 IP地址。
# 元组中的第二个元素为 端口号。http的端口为80
socketXL.connect(("news.sina.com.cn", 80))
# 3、发送请求，需要请求新浪新闻首页，并返回请求的数据内容。
# 注：send需要的参数为字节类型的参数
'''
GET / HTTP/1.1\r\nHost:news.sina.com.cn\r\nConnection:close\r\n\r\n
GET:表示请求方式，直接从服务器获取数据(速度较快)
请求数据常用的方式为：GET，POST，PUT，DELETE...
/ : /后面为url(网址)路径
HTTP/1.1 : 协议及协议版本，使用HTTP协议的1.1的版本。
Host:news.sina.com.cn：请求的IP地址为news.sina.com.cn
Connection:close：请求结束后自动关闭链接。

\r\n:每个请求头使用\r\n分隔
\r\n\r\n:当为两对\r\n时，将请求头与请求体分隔。
'''
socketXL.send(b"GET / HTTP/1.1\r\nHost:news.sina.com.cn\r\nConnection:close\r\n\r\n")

# 4、接收数据
# 用于接收IP包的数据
dataList = []
while True:
    # 接收数据  recv
    # 1024:对多接收1024个字节的数据
    # 接收到的数据类型：为字节类型
    conn = socketXL.recv(1024)
    # 如果接收的数据长度为0，代表数据接收完成。
    if len(conn) == 0:
        break
    # 将数据依次放到列表中
    dataList.append(conn)
# 5、将IP包数据拼接为完整的数据
data = b"".join(dataList)
# 6、将字节进行解码：decode("utf-8")
dataStr = data.decode("utf-8")
# 7、当数据请求结束时，关闭socket链接
socketXL.close()
# print(dataStr)
# 8、处理请求的数据
header, body = dataStr.split("\r\n\r\n", 1)
# print(header)
print(body)
