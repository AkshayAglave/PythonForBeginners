print("Hello, world!")
# dont explicitely declare data types
var = 42
print("The variable value is", var)
var = 43
print("The updated variable value is", var)

float_var = 3.14
print("The float variable value is", float_var)

bool_var = True
print("The boolean variable value is", bool_var)

print(type(bool_var))
# A Variable can hold different values
bool_var = 15;
print(type(bool_var))

# Mathematical operators

addition = 3+4
sub =7-3 
division = 15/3 #5
multiplication = 3*4  #12
modulo= 7%3 # 1

#Assignment operators

#Operator Precedence

#String

# Access by Indexing,Slices,concatenation, repetition
str1 = "Hello"
str2 = "World"

print(str1[0])

print(str2[1:4])

print(str1 + " " + str2)

print(str1 * 3)

#Convert to String

num = 100
str_num = str(num)
print("The number is " + str_num)

#Covert to Integer
str_value = "250"
int_value = int(str_value)
print("The integer value is", int_value)    