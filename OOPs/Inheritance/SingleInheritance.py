#Single inheritance: One parent -> One child
class Animal: #Parent
    def eat(self):
        print("This animal eats food")

class Dog(Animal): #Child
    def bark(self):
        print("Dog barks")

d = Dog()
d.eat() #Inherited from parent class
d.bark() #Child's own method

# Code reusability
# Cleaner structure
# Easy maintenance
# Represents real-world relationships (IS-A)