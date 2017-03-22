number = int(input("please enter a non-negative number to take the factorial of"))
product = 1
for i in range(number):
    product = product * (i+1)
print (product)    
