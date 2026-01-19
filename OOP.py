#OOP is way of writing programs by modeling real-world things as object
#Example:
    #Car: Object
    #Properties(color, speed): Variables
    #Actions(drive, brake): Functions

#Class: It's just a blueprint or a template, not a real-world entity
#Ex: A class "Student" defines what a student has and does
class Student:
    def __init__(self, name, age): #Constructor: Automatically runs when an object is created
        self.name = name #self: Refers to current object: Must be the 1st parameter
        self.age = age

    def __str__(self): #Method: Behavior: (Functions inside a class)
        return f"Student (name = {self.name}, age = {self.age})"


s1 = Student("Alice",21)
s2 = Student("Bob",22)
print(s1) #It will print useful human-readable output because of (__str__) method, used in class, otherwise it will just throw useless memory address, if missing it will fall back to (__repr__) which is Developer-Readable output
print(s2)