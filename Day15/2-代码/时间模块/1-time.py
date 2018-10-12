# time 时间
# 导入时间模块
import time
'''
开发中使用世界标准时间  UTC
中国 东八区  UTC+8   中国标准时间
1、时间戳
以浮点数或整数表示时间，以秒为单位，以1970年1月1日0时0分0秒开始计算

2、时间元组
tm_year  年 
tm_mon 月 
tm_mday 日
tm_hour 时 
tm_min 分 
tm_sec 秒 
tm_wday 一周中的第几天 
tm_yday  一年中的第几天 
tm_isdst 夏令时


3、格式化时间符号
%a:简化的星期名称
%A:完整的星期名称
%B:完整的月份名称
%c:本地时间用日期与时间表示
%d:一个月中的第几天   **
%H:时   **
%j:一年中的第几天
%M:分钟  **
%m: 月份  **
%p:上下午
%S：秒数  **
%W：本年的第几周
%w：一周中的第几天
%x：时间   年/月/日
%X：时间   时:分:秒
%y:简化的年份   **
%Y:完整的年份  **
'''

# 返回时间戳,浮点数
c = time.time()
print(c)

# 将时间戳转为UTC时间元组
t = time.gmtime(c)
print(t)

# 将时间戳转为本地时间元组
l = time.localtime(c)
print(l)

# 将时间元组转为时间戳
b = time.mktime(l)
print(b)

# 将本地时间元组转为时间字符串
tStr = time.asctime(l)
print(tStr)  # Mon Aug  6 09:41:00 2018
print(type(tStr))

# 将时间戳转为时间字符串
cStr = time.ctime(c)
print(cStr)

# 将时间元组格式化指定的字符串格式
# time.strftime("格式化时间格式", 时间元组)
sStr = time.strftime("%Y    %m    %d", l)
print(sStr)

# 将时间字符串转为时间元组
pTime = time.strptime(sStr, "%Y    %m    %d")
print(pTime)



# 延迟运行 ： 阻塞程序运行
print("我开始睡了")
time.sleep(5)
print("我睡醒了")

# 倒计时 10s

