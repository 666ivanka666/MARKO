# Write a program that loads two integers and an operation from the user. Valid operations are +, -, * and /. 
# Print the result of the operation nicely formatted, with conditions:
# If the operation is not correct, print an error.
# If the second number is 0 and the operation is division, print an error.


number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))
operation = input("Enter an operation (+, -, *, /): ")

if operation == "+":
     result = number_1 + number_2
elif operation == "-":
     result = number_1 - number_2
elif operation == "*":
    result = number_1 * number_2
elif operation == "/":
   if number_2 == 0:
      print("Error: Cannot divide by 0")
   else:
      result = number_1 / number_2
else:
       print("Error: Invalid operation entered. Valid operations are +, -, *, and /.")

if "result" in locals():
     print(f"Result: {result}")

# Write a program that loads a sentence.
# If there is a word "red" in the sentence then check if the last word in the sentence is "pill", and output "Accept life-changing facts". 
# If there is a word "blue" in the sentence then check if the last word in the sentence is "pill", and output "Remain ignorant".
# In "red" and "blue" case, if the second word is not "pill", then output "Red and blue are colors".

sentence = input("Enter a sentence: ").lower()

words = sentence.split()

if "red" in words:
    if words[-1] == "pill":
        print("Accept life-changing facts")
    else:
        print("Red and blue are colors")
elif "blue" in words:
    if words[-1] == "pill":
        print("Remain ignorant")
    else:
        print("Red and blue are colors")
else:
    print("Red and blue are colors")


# Write a program that will accept numbers and just for odd ones print squared values. Allow the program to exit on `q`.

# Explanation:
#   * In an endless loop, keep entering values.
#   * If value is `q`, then quit the program.
#   * Else, try to convert it to number. If it's an odd number, print its squared value.



while True:
    num = input("Enter a number or 'q' to quit: ")
    if num == 'q':
        break

    try:
        num = int(num)
        if num % 2 != 0:
            print(num ** 2)
    except ValueError:
        print("Please enter a valid number or 'q' to quit.")


# Write a program that draws a triangle like this:
# ```
#   *
#   * *
#   * * *
#   * * * *
#   * * * * *
#
# Need to use loops, and create program in order that user need to insert character, and with inserted character draw a triangle

char = input("Enter a character: ")
height = 5

for i in range(height):
    print(char * (i+1))
