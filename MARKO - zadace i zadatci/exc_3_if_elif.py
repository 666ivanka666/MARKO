

# Write a program that loads an integer from the keyboard and prints whether it is divisible by 3, 5, 7 and 11. 
# If program finds e.g. that it's divisible by 3, it should skip other checks. 
# It should work the same for all the cases.

a = int(input("Unesi a: "))

if a % 3 == 0:
    print("Broj je dijeljiv sa 3")
    
elif a % 5 == 0:
    print("Broj je dijeljiv sa 5")
elif a % 7 == 0:
    print("Broj je dijeljiv sa 7")
else:
    print("Broj nije dijeljiv sa 3, 5, 7 i 11")


# Change the last program (01-exercises.py) in the way that it always checks all the conditions. 
# Meaning, if program finds e.g. that it's divisible by 3, it should check also if it's divisible by other numbers.

a = int(input("Unesi a: "))

if a % 3 == 0:
    print("Broj je djeljiv sa 3")
if a % 5 == 0:
    print("Broj je djeljiv sa 5")
if a % 7 == 0:
    print("Broj je djeljiv sa 7")
if a % 11 == 0:
    print("Broj je djeljiv sa 11")

if a % 3 != 0 and a % 5 != 0 and a % 7 != 0 and a % 11 != 0:
    print("Broj nije djeljiv sa 3, 5, 7, niti 11.")



# Write a program that loads three integers from the keyboard and prints the largest of them.

a = int(input("Unesi a: "))
b = int(input("Unesi b: "))
c = int(input("Unesi c: "))

# a = 2
# b = 10
# c = 4

if a == b == c:
    print("Sva tri broja su jednaka.")
else:
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    else:
        print(c)



# Write a program that loads a number from the keyboard and prints whether it is even or odd.

a = int(input("Unesi a: "))

if a % 2 != 0:
    print("Broj je neparan")
else:
    print("Broj je paran")


# Write a program that loads two numbers (enumerated as 1 and 2) from the keyboard and if first one is greater prints "Number 1 is greater", 
# and vice versa. If they are the same print "Numbers are the same".
a = int(input("Unesi  broj 1: "))
b = int(input("Unesi  broj 2: "))

if a > b:
    print("Number 1 is greater")
elif a < b:
    print("Number 2 is greater")
else:
    print("Numbers are the same")


# Write a program that asks for a command. If command is...

# "run", print output "Running...",
# "stop" print output "Done."
# "pause", "repeat" or "skip" print which command is executed (e.g. "Executing command: pause").
#  Use or operator here.
#  something else, print the command along with the information that is unknown (e.g. "Unknown command: qwe").


command_input = input('Enter command ("run", "stop", "pause", "repeat", "skip"): ').lower()

if command_input == "run":
    print("Running...")
elif command_input == "stop":
    print("Done.")
elif command_input in ("pause", "repeat", "skip"):
    print(f"Executing command: {command_input}")
else:
    print("Unknown command:", command_input)


# Write a program that loads an integer from the keyboard and prints whether it is divisible by 3 or 7. 
# Otherwise it prints the message "The loaded number is divisible neither by 3 nor by 7".

number_input= int(input("enter number: "))


if number_input % 3 ==0:
     print("Number is divisible by 3")
elif number_input % 7 ==0:
     print("Number is divisible by 7")

else:
       print("The loaded number is divisible neither by 3 nor by 7")


