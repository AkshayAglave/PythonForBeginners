#FizzBuzz Challenge
for num in range(1, 50) :
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

#Factorial Challenge
        def factorial(n):
            result = 1
            for i in range(1, n + 1):
                result *= i
            return result

        # Testing the factorial function

        print("Factorial of 5:", factorial(3))
        print("Factorial of 7:", factorial(4))
        print("Factorial of 6:", factorial(5))

        #Reverse a String Challenge

        def reverse_string(string):
            reversed_string = ""
            for char in string:
                reversed_string = char + reversed_string
            return reversed_string

        # Testing the reverse_string function
        print("Reversed string of 'Hello':", reverse_string("Hello"))


        #Word Count Challenge

import re

def wordCounter(sentence):
    sentence.strip()
    # Split the sentence into words using regex to match whitespace

    words = re.split(r"\s+")
    return len(words)

# Testing the wordCounter function
test_sentence = "Hello world! Welcome to   Python programming."
print("Number of words in the sentence:", wordCounter(test_sentence))