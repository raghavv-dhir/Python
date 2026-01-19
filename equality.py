#Is (Identity: Same Object in memory), It checks: Are both references pointing to the same object?
#Example:
a = [1,2,3,4,5]
b = a          # b is just another name of a, thus pointing to same memory location
print (a is b) #True
print (a == b) #Checks values/data, as reference is same, thus data will also be same

a1 = [1,2,3,4,5]
b1 = [1,2,3,4,5] #Even though values are same, memory is different
print (a1 is b1) #False
print(a1 == b1)  #same values