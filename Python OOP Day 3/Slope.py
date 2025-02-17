class Slope:
    def __init__(self,x1,x2,y1,y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    def calcslope(self):
        d=(self.y2-self.y1)/(self.x2-self.x1)
        print("Slope : ",d)
ob1= Slope(2,4,6,5)
ob1.calcslope()
        