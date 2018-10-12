'''
网络概述：
使用网络的目的：
    为了多方用户进行共享数据。
    如果需要实现共享数据目的，就需要借助网络功能。
什么是网络？
    网络就是链接双方或多方的一种工具。

TCP/IP简介：
什么是协议？
    双方多方均认可并执行的规则。
什么是计算机/网络协议？
    计算机之间的沟通的规则。
计算机使用什么协议？
    计算机之间遵守的协议为TCP/IP协议。
TCP/IP协议：
    现代社会为了将计算机之间链接起来，制定了一套全球通用协议，是一套
    完整的通用协议标准。
    整套标准包含上百种协议，但最重要的协议就是TCP与IP两个协议，所以，
    后来将网络协议简称为TCP/IP协议。
IP地址： 协议标准 http/https   IP地址   端口号
http://www.baidu.com

IP地址：
    作为电脑的唯一标识。123.123.123.124
    IP地址对应网络链接接口的一个确定的目标。
IPv4：以字符串形式表示IP地址，表现形式：0-255.0-255.0-255.0-255
        32位整数。
IPv6：以字符串形式表示IP地址，
        表现形式：1111:2222:5555:abcd:1111:2222:5555:abcd
        128位整数。

IP协议：
    负责将数据从一台计算机传送到另一台计算机，数据会被分割成一块
    一块的，通过IP包的形式发送。
IP包的特点：本身以块的形式发送数据，但不能保证全部到达，也不能保证按
顺序到达。

TCP协议：
    建立IP协议之上，负责将数据从一台计算机传送到另一台计算机，会将计
    算机与计算机之间建立可靠的链接，能够保证数据按顺序到达，如果数据出现
    丢失，会自动重新建立链接。

端口号：
端口是通过端口号来标记区分的，端口号只是整数：0-65535
端口主要用来区分不同的程序。

知名端口：
80：分配给HTTP服务的
21：分配给FTP服务的

0-3000    6666   8888


http://www.hggg.com:6789

10.31.151.70
飞Q   QQ   微信   探探     10.31.151.70:80
飞Q   QQ   微信   探探     10.31.151.71:80


70   ----  服务器   ---- 71 端口号

一个完整的IP地址：
协议     IP            端口号
http://123.123.123.123:8080

系统程序默认的端口号可以省略不写。
'''