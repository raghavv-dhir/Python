#Abstarction: Hiding the implementation details of the class and only showing the essential features to the user
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.cluth = False

    def start(self):
        self.acc = True
        self.cluth = True
        print("Car started...")


c1 = Car()
c1.start()

