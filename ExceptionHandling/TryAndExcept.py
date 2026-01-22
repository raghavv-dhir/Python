#Try and Except Keywords
#TRY: The 'try' block contains the code which might throw an exception. If an exception occurs in this block, it is passed to the except block for handling.

#Except: The except block is used to catch and handle the exception that occurs in the try block. We can have multiple except blocks for different types of exception, but order matters, Exception class is the parent of all types of exceptions
num = 10

try:
    import mat
    den = int(input("Enter denominator: "))
    print(num / den)  #If den = 0, it will be handled by except block

except ZeroDivisionError as e: #Handler for zero division
    print("Please provide an integer except zero: ",e)

except ValueError as e:
    print("Please provide a numeric value: ",e) #Handler for value error
    #print("Oops, something went wrong!") #But, here we should have handled different errors specifically like ZeroDivisionError, ValueError etc. and not just something went wrong.

except Exception as e: #order matters, because it's the parent class
    print(e)

print("Thank you for using this program") #This part will now run smoothly even if any error occurs above, flow is not disturbed