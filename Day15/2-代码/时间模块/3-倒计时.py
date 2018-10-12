# 每隔1秒数字减1，当为0时，输出重新发送
# 1s
import time
for x in range(4):
    print("%s s" % (4-x-1))
    time.sleep(1)
    # if (4-x-1) == 0:
    #     print("链接")
else:
    print("重新链接")


