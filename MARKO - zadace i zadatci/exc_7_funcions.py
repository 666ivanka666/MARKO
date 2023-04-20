# Write two functions that accept two integers:
#   one that returns the product of two integers (print it afterwards)
#   one that prints the product of two integers and does not return it

def multiply_and_return(a, b):
    product = a * b
    return product

def multiply_and_print(a, b):
    product = a * b
    print(product)

result = multiply_and_return(5, 6)
print(result)

multiply_and_print(10, 20)

# Write a function that accepts an integer n and returns the sum of the numbers from 1 to n. 
# To call the function, load integer n from the user.
# Then change the function call to use a keyword argument.


def sum_numbers(n):
    return sum(range(1, n+1))

n = int(input("Enter an integer: "))
print(sum_numbers(n))


# Write a function that keeps loading numbers from the user as long as the sum of the already loaded numbers is less than or equal to 100. 
# Inside the function, print the sum of the numbers. The function returns how many numbers were entered from the user. 
# Print the number of entered numbers in the main part of the program.

def load_numbers():
    total = 0
    count = 0
    while total <= 100:
        num = int(input("Enter a number: "))
        total += num
        count += 1
        print(f"Current sum: {total}")
    return count

num_entered = load_numbers()
print(f"Number of entered numbers: {num_entered}")


# Write a function that receives a sentence and a character and returns how many times the given character appears in the sentence. 
# If character is not given, default it to "a".

def count_characters(sentence, character='a'):
    return sentence.count(character)

sentence =input('Sentence is: ')
character = "s"
count = count_characters(sentence, character)
print(count)  

count_a = count_characters(sentence)
print(count_a)  

# Write two functions:
#   - a function that generates list of 5 random numbers between 1 and 20
#   - a function that returns the average of the received numbers in list

# In the main part of the program, use these functions to generate list and calculate the average of the list.
# After generation, print list items in a single row.

import random

def generate_random_numbers():
    return random.sample(range(1, 21), 5)

def calculate_average(numbers):
    return sum(numbers) / len(numbers)


numbers = generate_random_numbers()
average = calculate_average(numbers)


print(*numbers,sep=',')
print("average of the numbers: ",average)


# Write a function that takes a word and returns the same word with a parameterized character 
# between every two characters. 

# For example, if a function receives "table" and "_", let it return "t_a_b_l_e".
# For example, if a function receives "word" and "+", let it return "w+o+r+d".

# Let the default characters be "-".
# Call the function using keyword arguments.'''

def add_separator(word, separator='-'):
    
    return separator.join(word)


print(add_separator("table", "_")) # "t_a_b_l_e"
print(add_separator("word", "+")) # "w+o+r+d"
print(add_separator("python")) # "p-y-t-h-o-n"
