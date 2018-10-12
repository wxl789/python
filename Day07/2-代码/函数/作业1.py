# 1、拆分字符串：
# https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1
# &tn=baidu&rsv_pq=d87daf&rqlang=cn
# 拆分的结论为：
# {"ie":"utf-8", "f":"8", "rsv_bp":"0", "rsv_idx":"1", "tn":"baidu",
# "rsv_pq":"d87daf", "rqlang":"cn"}
str1 = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&rsv_pq=d87daf&rqlang=cn"
print(str1.find("?"))
str2 = str1[24:]
list1 = str2.split("&")
print(list1)
dict1 = {}
a = " "
for i in range(len(list1)):
    a = list1[i].split("=")
    dict1[a[0]]=a[1]
print(dict1)




