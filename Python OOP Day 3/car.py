class Car:
    def __init__ (self,modelname,color,year):
        self.modelname = modelname
        self.color = color
        self.year = year
    def display(self):
        print("Car model :",self.modelname,"Car color : ",self.color,"Car Year :",self.year)

c1 = Car("Mahindra Thar","Grey",2020)
c1.display()