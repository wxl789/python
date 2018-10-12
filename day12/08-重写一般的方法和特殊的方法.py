
class A:

    def hello(self):
        print("hello")

class B(A):
    def hello(self):
        print("wolrd")
a = A()
a.hello()
b = B()
b.hello()


class Bird(object):
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print(",,,,,")
            self.hungry = False
        else:
            print("no thanks")
b = Bird()
b.eat()
b.eat()






