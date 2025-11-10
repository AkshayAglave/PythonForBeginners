#Example to show flow statements
age = 18
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
#Using elif same as else if in java
marks = 85
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: D")

    #truthy and falsy values with detailed examples
value = 0
if value:
    print("The value is truthy.")
else:
    print("The value is falsy.")        
value = 42
if value:
    print("The value is truthy.")
else:
    print("The value is falsy.")        
text = ""
if text:
    print("The text is truthy.")
else:
    print("The text is falsy.")
text = "Hello"

#explanation of bool() function

if text:
    print("The text is truthy.")
else:
    print("The text is falsy.")
#Using bool() function to check truthy/falsy
print("Is 0 truthy?", bool(0))
print("Is 42 truthy?", bool(42))
print("Is empty string truthy?", bool(""))
print("Is 'Hello' truthy?", bool("Hello"))
#

#Loops in Python

print("Using while loop to print numbers from 1 to 5")
count = 1
while count <= 5:
    print(count)
    count += 1

print("Using for loop to iterate over a list")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("I like", fruit)
print("Using for loop with range to print numbers from 0 to 4")
for i in range(5):
    print(i)

    # range() method explanation
print("Using range() with start and end")
for i in range(2, 6):
    print(i)    