
class People(object):

    address = "杭州"
    @staticmethod
    def getAddress():
        return People.address

print(People.address)

print(People.getAddress())

p = People()
print(p.getAddress())
