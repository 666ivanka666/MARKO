# Write a program that inputs two strings, swaps their values using tuples and outputs them.

string1 = input('Enter first string: ')
string2 = input('Enter second string: ')


string1, string2 = string2, string1

print('After swapping:')
print('First string:', string1)
print('Second string:', string2)


# Write a program that initializes 3 strings and starts the for loop that runs 10 times. 
# In for loop, it rotates 3 strings (str1=> str2, str2=>str3, str3=>str1) using tuples and writes strings in the same line, with number of iteration: 

# 0: str1 str2 str3
# 1: str3 str1 str2
# 2: str2 str3 str1

string1 = input('first string: ')
string2 = input('second string: ')
string3 = input('third string: ')

for i in range(10):
    print(f"{i}: {string1} {string2} {string3}")
    string1, string2, string3 = string3, string1, string2

   
# Write a program that asks for two strings.
# Then it should print the following:

# - all characters that can be found in strings, but without repetition (for 'abc' and 'bcd', it should print 'abcd')
# - all the characters that exist in both strings (for 'abc' and 'bcd', it should print 'bc')
# - all the characters that exist in first but not in second string (for 'abc' and 'bcd', it should print 'a')
# - all characters in strings, but but without intersection (for 'abc' and 'bcd', it should print 'ad')

string1 = input('Enter the first string: ')
string2 = input('Enter the second string: ')

all_chars = ''.join(set(string1 + string2))


common_chars = ''.join(set(string1) & set(string2))
first_only_chars = ''.join(set(string1) - set(string2))
unique_chars = ''.join(set(string1) ^ set(string2))

print("All characters without repetition: ", all_chars)
print("Common characters in both strings: ", common_chars)
print("Characters in the first string but not in the second: ", first_only_chars)
print("Characters without intersection: ", unique_chars)




# Write a program to enter survey data on students and their favorite programming language (key: name, value: favorite programming language).
# Allow the user to enter survey results as long as he wants. Ensure that survey entries are unique (the key to making the survey unique is the username). 

# Print the survey results in the form:
# - Name:
# - Favorite language:


survey = {} 

while True:
  
  name = input('Enter the name: ')
  language = input('Enter the favorite language: ')


  survey[name] = language

  more = input('Do you want to enter more survey results (y/n)? ')
  if more.lower() != 'y':
    break

for name, language in survey.items():
  print(f'Name: {name} favorite language is: {language}')



# Write a program that will parse the following string: `key1=value1;key2=value2;key3=value3`.
# Use an appropriate structure for that.

s = 'key1=value1;key2=value2;key3=value3'
items = s.split(';')  

parsed = {}

for item in items:
  key, value = item.split('=')  
  parsed[key] = value

print(parsed)





