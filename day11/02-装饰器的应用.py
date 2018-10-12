
#定义一个函数，完成包裹数据
def makeBold(fn):#fn---demo1
    def warpped():
        return "<b>"+fn()+"</b>"
    return warpped

def makeitalic(fn):
    def warpped():
        return "<i>"+fn()+"</i>"
    return warpped
print("--------------aaaaaaaaaaaaaaaaaaaaaaaaaa--------------------------------")
@makeBold
def demo1():
    return "hello world-1"

print(demo1())

@makeitalic
def demo2():
    return "hello world-2"
print(demo2())


@makeBold
@makeitalic
def demo3():
    return "hello world-3"

print(demo3())









