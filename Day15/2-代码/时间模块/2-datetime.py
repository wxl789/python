# datetime比time高级很多，datetime时time的二次封装

# 导入datetime
import datetime

# 获取本地时间
# datetime:模块  datetime：类名  now():类方法
nowTime = datetime.datetime.now()
print(nowTime)
print(type(nowTime))  # datetime.datetime

# 返回指定时间
zTime = datetime.datetime(year=2018, month=2, day=14, hour=7, minute=23,
                          second=45, microsecond=876)
print(zTime)

# 将时间类型转为指定字符串类型
tStr = nowTime.strftime("%y  %m  %d")
print(tStr)

# 将时间字符串转为时间类型
# datetime.datetime.strptime(时间字符串, "格式化时间格式")
t = datetime.datetime.strptime(tStr, "%y  %m  %d")
print(t)


# 时间的运算  减法运算
d1 = nowTime - zTime
# 获取间隔天数与时分秒
print(d1)
# 获取间隔天数
print(d1.days)
# 获取除天数以外的秒数
print(d1.seconds)


# 时间类型数据   ---   strftime    ---   时间字符串
# 时间字符串   ---   strptime    ---   时间类型数据