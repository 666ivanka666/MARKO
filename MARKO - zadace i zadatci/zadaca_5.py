# Write a function that prints characters with ASCII codes from 65 to 70.
# Then write a function that returns characters with ASCII codes from 65 to 70.
# Then change that function to receive one parameter n, and return characters with ASCII codes from 65 to 65+n.

def print_ascii():
    for i in range(65, 71):
        print(chr(i))

def return_ascii():
    return ''.join([chr(i) for i in range(65, 71)])


def return_ascii_n(n):
    return ''.join([chr(i) for i in range(65, 66+n)])



# Write a function that takes a string input. If the string input is longer than 
# 10 characters or shorter than 3 characters, return None. Otherwise return lowercase string.
string =input('string is :')
def process_string(string):
    if len(string) > 10 or len(string) < 3:
        return None
    else:
        return string.lower()

result = process_string(string)
print(result)

# Write a function that takes a sentence as an argument and _prints_ number of words in it.
def count_words(sentence):
    words = sentence.split()
    return len(words)

sentence = "sidi di si ni za di si nisi"
num_words = count_words(sentence)
print(f"The sentence '{sentence}' has {num_words} words")

# Write a function that calculates and returns triangle area, `P = 0.5 * base * height`


def triangle_area(base, height):
    area = 0.5 * base * height
    return area


# Write a function that takes a sentence as an argument and returns average length of a word, rounded to nearest integer (use `round(x)`). 
# When function returns, print the returned value in the format "Average length of word is: 5" .

def average_word_length(sentence: str) -> int:
    words = sentence.split()
    total_length = sum(len(word) for word in words)
    average_length = total_length / len(words)
    return round(average_length)

sentence = input("Enter a sentence: ")
avg_length = average_word_length(sentence)
print(f"Average length of word is: {avg_length}")


# Write a function that takes a word as an input.
#   If the word is shorter than 4 characters, pad it with `*` character to the length 4.
#   If the word is longer than 4 characters, truncate it.

# Then:
#   - convert the sentence "The quick brown fox jumps over the lazy dog" to list of words
#   - for each word call the implemented function and print the result 

def word_lng(word):
    if len(word) < 4:
        return word.ljust(4, '*')
    else:
        return word[:4]

sentence = "The quick brown fox jumps over the lazy dog"
words = sentence.split()
for word in words:
    print(word_lng(word))


# Write a function that calculates the volume of the cylinder: `V = 2 * r * PI * h`
# Function receives parameters `r` and `h` and returns the result.
# Call the function using keyword arguments.
# If argument `h` is not given, default it to 10.
import math

def cylinder_volume(r, h=10):
    return 2 * r * math.pi * h

print(cylinder_volume(r=5))  
print(cylinder_volume(r=5, h=20)) 

# Write a function that gathers keyword arguments and returns them in the following format:
# Example: `arg1=val1;arg2=val2;arg3=val3`

def gather_kwargs(**kwargs):
    args = ";".join(f"{k}={v}" for k, v in kwargs.items())
    return args

print(gather_kwargs(arg1=1, arg2='two', arg3=[3, 3, 3]))

# Write a program that calculates the perimeter and area of a right-angled triangle.
# Allow the user to choose whether they want to input legs (catheti), perimeter, or area as long as they want.
# Use functions to print menus, calculate hypotenuse, calculate area and calculate perimeter.
from math import sqrt

def print_menu():
    print("1. Input legs (catheti)")
    print("2. Input perimeter")
    print("3. Input area")

def calculate_hypotenuse(a, b):
    return sqrt(a ** 2 + b ** 2)

def calculate_area(a, b):
    return (a * b) / 2

def calculate_perimeter(a, b, c):
    return a + b + c

while True:
    print_menu()
    choice = int(input("Choose an option: "))

    if choice == 1:
        a, b = map(float, input("Enter the length of the first and second leg separated by a space: ").split())
        c = calculate_hypotenuse(a, b)
        print(f"Hypotenuse: {c}")
        print(f"Area: {calculate_area(a, b)}")
        print(f"Perimeter: {calculate_perimeter(a, b, c)}")

    elif choice == 2:
        p = float(input("Enter the perimeter: "))
        a = float(input("Enter the length of the first leg: "))
        b = p / 2 - a
        c = calculate_hypotenuse(a, b)
        print(f"Legs: {a}, {b}")
        print(f"Hypotenuse: {c}")
        print(f"Area: {calculate_area(a, b)}")

    elif choice == 3:
        area = float(input("Enter the area: "))
        a = float(input("Enter the length of the first leg: "))
        b = 2 * area / a
        c = calculate_hypotenuse(a, b)
        print(f"Legs: {a}, {b}")
        print(f"Hypotenuse: {c}")
        print(f"Perimeter: {calculate_perimeter(a, b, c)}")

    else:
        print("Invalid choice. Please try again.")
