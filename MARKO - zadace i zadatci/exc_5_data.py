# Write a program that initializes the list with 5 names.
# Reverse each name using a for loop, and print original and reversed list.

arr = ["Ivanka", "Marko", "Matija", "Josip", "Luka"]
arr_rev = []

for a in arr:
    arr_rev.append(a[::-1])

print("Original list:", arr)
print("Reversed list:", arr_rev)



# Start with the previous example.
# For each name in original list print also its index, 
# and the item at that index in reversed name list.

arr = ["Ivanka", "Marko", "Matija", "Petar", "Ivo"]
arr_rev = []

for a in arr:
    arr_rev.append(a[::-1])

list_len = len(arr) # 5

for idx in range(list_len):
    print(f"Index: {idx}, Name: {arr[idx]}, Reversed name: {arr_rev[idx]}")


# Write a program in which you fill the list with 100 random numbers between 1 and 1000. 
# Print how many even elements are there in a list.
# Then remove all the odd elements and count again how many elements are there in a list.

import random

random_numbers = [random.randint(1, 1000) for _ in range(100)]

counter = 0
for i in range(len(random_numbers)):
    if random_numbers[i] % 2 == 0:
        counter += 1
print(f'Number of even elements: {counter}')

new_numbers = []
for i in range(len(random_numbers)):
    if random_numbers[i] % 2 == 0:
        new_numbers.append(random_numbers[i])


new_count = len(new_numbers)
print(f'Number of elements after removing odd elements: {new_count}')




# Create an empty dictionary. Load the user's 5 domain tags and the country to which the domain belongs to the dictionary. 
# After entering, print the contents of the dictionary in the format of country - domain name.

dictionary = {
    'moj posao.com': 'hrvatska',
    'moje delo.com': 'slovenija',
    'metro.at': 'ausrija',
    'calcedonia.it': 'italia',
    'footlocker.de': 'njemacka'
}

for domain, country in dictionary.items():
    print(f'{country} - {domain}')


# Upgrade previous program (04-exercise), after input, allow the user to search endlessly by domain tag. 
# If the domain does not exist in the dictionary, inform the user about it.


while True:
    tag = input("Enter a domain (type 'q' to quit): ")
    if tag == 'q':
        break
    if tag in dictionary:
        print(f'{tag} belongs to {dictionary[tag]}')
    else:
        print(f'{tag} does not exist in the dictionary')



# Write a program that will for each letter of the alphabet store its ASCII code. Print the contents of the data structure.


test_str = "abcdefghijklmnopqrstuvwxyz"
print(ascii(test_str))

alphabet = 'abcdefghijklmnopqrstuvwxyz'

ascii_codes = {}

for letter in alphabet:
  ascii_codes[letter] = ord(letter)

print(ascii_codes)