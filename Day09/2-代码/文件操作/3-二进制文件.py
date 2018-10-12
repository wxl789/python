# 写入文件   wb
# 将写入的字符串进行编码 encode()
with open(file="告白1.txt",mode="wb") as f1:
    # 编码
    str1 = "北京有沙尘暴"
    f1.write(str1.encode("gbk"))

# 读取文件
# 解码  decode()
with open(file="告白1.txt", mode="rb") as f2:
    data = f2.read()
    print(data)
    print(type(data))  # bytes  字节类型
    # 解码
    str1 = data.decode("gbk")
    print(str1)