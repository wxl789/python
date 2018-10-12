def func3():
    print("module--3")
def func4():
    print("module -- name")

# __name__ 属性
if __name__ == "__main__":
    func3()
else:
    func4()
    print(__name__)
