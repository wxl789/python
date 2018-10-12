# 163邮箱

# 发送邮件相关的模块
import smtplib
# 邮件文本
from email.mime.text import MIMEText
# 邮件标题
from email.header import Header

# smtp : 简单的邮件传输协议   Simple Mail Transfer Protocol

# 163邮箱的服务器地址
mailServer = "smtp.163.com"
# 163邮箱的服务器的端口号
mailPort = 25

# 连接smtp服务器,获取邮箱服务
smtp = smtplib.SMTP(host=mailServer, port=mailPort)

# 账号： 163邮箱账号
user = "15810008629@163.com"
# 密码：163邮箱的授权码
passwd = "123456q"

# 登陆邮箱
smtp.login(user=user, password=passwd)

# 发送邮件
# 发送者
sender = user
# 接收者
rec = "wlfww123@163.com"
# 邮件内容
str1 = "你好，交个朋友好不好，我是好人。"
'''
第一个参数：文本内容
第二个参数：文本格式
第三个参数：文本编码格式
'''
msg = MIMEText(str1, "plain", "utf-8")
# 标题
str2 = "告白情书2"
'''
第一个参数：标题内容
第二个参数：文本编码格式
'''
msg["Subject"] = Header(str2, "utf-8")
# 设置收件人名称
msg["to"] = rec
# 设置发件人名称
msg["from"] = sender

# 发送邮件
smtp.sendmail(sender, rec, msg.as_string())

# 退出邮箱
smtp.quit()

# 554  535  邮件代码没问题，163默认将邮件作为垃圾邮件处理。












