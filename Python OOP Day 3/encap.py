class Base:
    def __init__(self):
        self.a="Hello"
        self.__c="World"
class Derive(Base):
    def __init__(self):
        Base.__init__(self)
        print("calling private member of class")
        print(self.__c)
o = Base()
b = Derive()
print(o.a)
print(__Derive__c)
