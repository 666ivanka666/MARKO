# Write a program that prints the numbers from 1 to 5 using a while loop. 
# Each number in a separate line

counter = 1

while counter <= 5:
    print(counter)
    counter += 1

# Write a program that prints the numbers from 1 to 5 using a while loop
# So that it prints the numbers one after another, delimited with space. 
# Example: 1 2 3 4 5

counter = 1

while counter <= 5:
    print(counter, end=" ")
    counter += 1

# Write a program that inputs a string that will be output in capital case (capitalized string).
# Program should run in an infinite loop.
# Specifically, if letter `q` is entered, program should exit

while True:
    word = input("Unesi rijec (q - za izlaz): ")
    if word == 'q':
        break
    else:
        print(word.capitalize())

# Write a program that asks for two numbers.
# If first number is smaller than the second one, increase it in loop until it get equal as the second one.
# If second number is smaller than the first one, increase it in loop until it get equal as the first one.
# At the end, write the values.


while True:
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        break
    except ValueError:
        print("Invalid input. Please enter integers only.")

if num1 < num2:
    while num1 < num2:
        num1 += 1
elif num2 < num1:
    while num2 < num1:
        num2 += 1
else:
    print("The two numbers are already equal.")

print("Final values: {} and {}".format(num1, num2))


#BONUS
# Change the last example so that it outputs all the even numbers between the given two numbers

print("Even numbers between the two values:")
for i in range(num1, num2+1):
    if i % 2 == 0:
        print(i)



# Write a program that prints numbers from 1 to 10 
# separated by *tabs* using a for loop.


counter = 1

while counter <= 10:
    print(counter, '\t')
    counter += 1

# Write a program that prints all odd numbers between 
# 10 and 30 separated by tabs using a for loop.

for i in range(11, 31, 2):
    print(i, end='\t')


# Write a program that manages a counter in an infinite loop.
# Counter starts from 0.
# Prompt for command should be `cmd>`

# Support these commands:
#   * `inc`: increase counter by 1
#   * `dec`: decrease counter by 1
#   * `rst`: resets counter to 0
#   * `quit`: ends the program
#   * if any unknown command is entered, ignore it

#   After any command except `quit` and unknown, output `ok` and the current counter value.

# Note: for last two points (`quit` and unknown) use `break` and `continue`


counter = 0

while True:
    cmd = input('cmd ("inc", "dec","rst", "quit"): ')

    if cmd == "inc":
        counter += 1
        print(counter)
    elif cmd == "dec":
        counter -= 1
        print(counter)
    elif cmd == "rst":
        counter = 0
        print(counter)
    elif cmd == "quit":
        break
    else:
        continue

  
# Write a program that prints the numbers from 1 to 5 using a while loop. 
# Each number in a separate line

counter = 1

while counter <= 5:
    print(counter)
    counter += 1


# Write a program that prints the numbers from 1 to 5 using a while loop
# So that it prints the numbers one after another, delimited with space. 
# Example: 1 2 3 4 5

counter = 1

while counter <= 5:
    print(counter, end=" ")
    counter += 1


# Write a program that inputs a string that will be output in capital case (capitalized string).
# Program should run in an infinite loop.
# Specifically, if letter `q` is entered, program should exit

while True:
    word = input("Unesi rijec (q - za izlaz): ")
    if word == 'q':
        break
    else:
        print(word.capitalize())

