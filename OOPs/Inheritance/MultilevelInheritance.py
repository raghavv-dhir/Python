#Grandparent -> Parent -> Child
class A:
    def showA(self):
        print("class A")

class B(A):
    def showB(self):
        print("class B")

class C(B):
    def showC(self):
        print("class C")

c = C()
c.showA()
c.showB()
c.showC()