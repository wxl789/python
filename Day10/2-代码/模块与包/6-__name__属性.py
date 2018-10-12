# __name__
# 属性

'''
每个模块本身就是一个可执行的.py文件，一个模块可以引入另一个模块。

每个模块都有一个__name__属性，当__name__属性的值为 '__main__'时，
代表该模块自己本身在运行，否则，被引入了其他模块。


'''
import module3

def main():
    print("main")
    print(__name__)

if __name__ == "__main__":
    main()


