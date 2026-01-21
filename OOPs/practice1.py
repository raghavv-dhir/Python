#Create student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod #Decorator (Changed its behavior)
    def hello(): #doesn't make a sense to use self here, as we are not dealing with objects, so this is a class-level function
        print("Hello!")

    def printAvg(self):
        sum = 0
        for mark in self.marks:
            sum += mark
        print(f"Hi, {self.name}, your average marks is: {sum/len(self.marks)}")


s1 = Student("Sarah", [100, 87, 94])
s1.hello()
s1.printAvg()
