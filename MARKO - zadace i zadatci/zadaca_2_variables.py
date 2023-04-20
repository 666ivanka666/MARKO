
 
# 1.Write a program that prints three words: "Hello", "World", "Python", each on its own line, separated by a blank line
# 1.Napišite program koji ispisuje tri riječi: "Zdravo", "Svijet", "Python", svaka na svojoj liniji, odvojena praznom linijom

print("Zdravo\n")
print("Svijet\n")
print("Python\n")



# 2.Store the value 52 in the variable named *number*. Print the variable on the screen.
# 2.Spremi vrijednost 52 u varijabli pod nazivom *broj*. Ispišite varijablu na zaslonu.

number = 52
print(number)


# #3. Write a program that stores the number 10 in one variable, the number 25 in another, and prints the sum, product, difference and quotient of these numbers. 
# #Napišite program koji pohranjuje broj 10 u jednu varijablu, broj 25 u drugoj i ispisuje zbroj, proizvod, razliku i kvocijent tih brojeva. 


number_1=10
number_2=25


print(number_1, "+", number_2, "=", (number_1 + number_2))
print(number_1, "-", number_2, "=", (number_1 - number_2))
print(number_1, "*", number_2, "=", (number_1 * number_2))
print(number_1, "/", number_2, "=", (number_1 / number_2))

# # Format the printout so that each printout is on its own line, and both the operands and the operator are printed. 
# # Oblikujte ispis tako da je svaki ispis u svom retku, a ispisuju se i operandi i operator. 

# # For example, for the product it is necessary to print: "10 * 25 = 250".
# # Na primjer, za proizvod je potrebno ispisati: "10 * 25 = 250

number_1= int(input("first number: "))
print(type(number_1))
number_2= int(input("second number: "))
print(type(number_2))


print(number_1, "+", number_2, "=", (number_1 + number_2))
print(number_1, "-", number_2, "=", (number_1 - number_2))
print(number_1, "*", number_2, "=", (number_1 * number_2))
print(number_1, "/", number_2, "=", (number_1 / number_2))


# # Questions:
# # What is string concatenation, and what ways we can do that (provide example for each ways based on task above)? Feel free to google that
# #Pitanja:
# # Što je ulančavanje nizova i na koje načine to možemo učiniti (pružiti primjer za svaki način na temelju gornjeg zadatka)? Slobodno guglajte to

# #ODGOVOR
#- spajanje varijabli na razne nacine 



#4. Write a program that loads the length of the sides of a rectangle and prints its area and perimeter.
#4. Napišite program koji učitava duljinu stranica pravokutnika i ispisuje njegovo područje i perimetar

l = float(input('Enter the length: ')) 
w = float(input('Enter the width: '))
 
area = l * w
perimeter = 2 * (l + w)

print("Area of the rectangle is:", area)
print("Perimeter of the rectangle is:", perimeter)

#5. Read a character from the user and draw something like this using that character (assuming that user entered *x*):
#
#|   x     |
#|  xxx    |
#| xxxxx   |
##5. Pročitajte znak od korisnika i nacrtajte nešto slično pomoću tog znaka (pod pretpostavkom da je korisnik unio *x*):
#
#|   x |
#|  xxx |
#| xxxxx |
#
char = input("Unesite znak: ")
print(f"|   {char}     |")
print(f"|  {char*3}    |")
print(f"|  {char*5}    |")







