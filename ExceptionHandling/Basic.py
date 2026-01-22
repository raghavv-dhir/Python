#Types of Errors:
#Syntax error (something wrong with the structure of the code): During compilation
#Exceptions/Runtime error: During execution
num = 2
den = 0
ans  = num / den
print(ans) #Here, exception will occur, therefore the code below will be lost.

#Avoid shutting down the full code
print("This line will not be executed unless the above error is not handled gracefully")
#We should handle the errors gracefully in perspective of the user (a non-technical person)
#Handling exception in Python:
#1. Try
#2. Except
#3. Else
#4. Finally

