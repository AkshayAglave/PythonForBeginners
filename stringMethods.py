#upper()
text = "hello world"
print(text.upper())

#lower()
text = "HELLO WORLD"
print(text.lower())

#isUpper()
text = "HELLO WORLD"
print(text.isupper())

#isLower()
text = "hello world"
print(text.islower())

#startswith()
text = "Hello, world!"
print(text.startswith("Hello")) 
#endswith()
text = "Hello, world!"
print(text.endswith("world!"))
#join()
words = ["Hello", "world", "from", "Python"]
sentence = " ".join(words)
print(sentence)     # Output: Hello world from Python

words = ["Hello", "world", "from", "Python"]
sentence = ".".join(words)
# Output: Hello.world.from.Python
print(sentence) 

demoText = "Hello"
demoText.join("World Python")
print(demoText)
#output: HelloWorld Python

#split()
text = "Hello, world! Welcome to Python."
words = text.split(" ")
print(words)

#strip()
#Explanation: The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)
text = "   Hello, world!   "
cleaned_text = text.strip()
print("[" + cleaned_text + "]")  # Output: [Hello, world!]  

#rstrip()
#Explanation: The rstrip() method removes any trailing characters (space is the default trailing character to remove)
text = "   Hello, world!   "
cleaned_text = text.rstrip()
print("[" + cleaned_text + "]")  # Output: [   Hello, world!]
#rstrip() with specific characters
text = "Hello, world!!!"
cleaned_text = text.rstrip("!")
print("[" + cleaned_text + "]")  # Output: [Hello, world]   
#lstrip()
#Explanation: The lstrip() method removes any leading characters (space is the default leading character to remove)
text = "   Hello, world!   "
cleaned_text = text.lstrip()
print("[" + cleaned_text + "]")  # Output: [Hello, world!

#replace()
#explanation: The replace() method replaces all occurrences of a specified substring with another substring.
text = "Hello, world! Welcome to the world of Python."
new_text = text.replace("world", "universe")
print(new_text)  # Output: Hello, universe! Welcome to the universe of Python.  


#len()
#explanation: The len() function returns the number of characters in a string.
text = "Hello, world!"
length = len(text)
print("Length of the text is", length)  # Output: Length of the text is 13


#Format()
name = input("Enter your name: ")
age = input("Enter your age: ")
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string) 