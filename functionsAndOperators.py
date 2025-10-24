#Defining and calling functions in Python

def greet(name):
    print("Hello,", name)

greet("Raj")

def add(a, b):
    return a + b   
sum = add(5, 7)
print("The sum is", sum)
#We can also have default parameters
def add(a, b=10):
    return a + b    
sum = add(5)
print("The sum with default parameter is", sum) 