class Person(object):
    def __init__(self,name,idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(f"My name is {self.name}")
        print("Idnumber is {} ".format(self.idnumber))

#child class
class employee(Person):
    def __init__(self,name,idnumber,salary,post):
        self.salary = salary
        self.post = post
        Person.__init__(self,name,idnumber)
    def details(self):
        print(f"My name is {self.name}")
        print("Idnumber is {} ".format(self.idnumber))
        print(f"My salary is {self.salary}")
        print("Post is {} ".format(self.post))

a = employee("Darshan",69,1000000,"Security Engineer ",)
a.details()

