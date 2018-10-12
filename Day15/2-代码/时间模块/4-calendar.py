# 导入日历模块
import calendar

# 返回指定年份的日历
print(calendar.calendar(2018))

# 返回指定年份及月份的日历
print(calendar.month(2018, 8))

# 判断平闰年  平年返回False  闰年返回True
print(calendar.isleap(2020))

# 返回某月第一天的星期的下标及本月的天数
print(calendar.monthrange(2018, 8))

# 以列表的形式返回日历
print(calendar.monthcalendar(2018,8))

