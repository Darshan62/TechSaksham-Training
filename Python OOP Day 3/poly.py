class Bird:
    def intro(self):
        print("There are different types of birds")
    def flight(self):
        print("Most of the birds can fly but some cannot")

class sparrow(Bird):
    def flight(self):
        print("Sparrows can fly")

class ostrich(Bird):
    def flight(self):
        print("Ostrich cannot fly")

b=Bird()
b_sp = sparrow()
b_os = ostrich()

b.intro()
b.flight()

b_sp.flight()
b_os.flight()
b_sp.intro()
b_os.intro()
