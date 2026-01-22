try:
    a = 10
    b = int(input("Enter a number: "))
    d = a + b
    c = a / b
    print("Division is: "+str(c))
    print("Sum is: "+str(d))

except ArithmeticError:
    print("ARTH")

except ZeroDivisionError:
    print("NOT-0")

print("END")
