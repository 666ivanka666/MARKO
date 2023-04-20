# Write a Python class to implement pow(x, n)
class Python:
    def __init__(self, x, n):
        self.x = x
        self.n = n
    def pow(self):
        return self.x ** self.n

# Write a Python class to reverse a string word by word.

class Python:
    def __init__(self, words):
        self.words = words
    
    def reverse_word(self):
        print ("word")
        for word in self.words:
            print (word [::-1])

## chat gpt
class ReverseString:
    def __init__(self, input_string):
        self.input_string = input_string
    
    def obrni_rijec_po_rijec(self):
        # razdvoji ulazni string u listu riječi
        words_list = self.input_string.split()
        
        # obrni redoslijed riječi u listi
        reversed_words_list = words_list[::-1]
        
        # spoji obrnute riječi natrag u jedan string
        reversed_string = " ".join(reversed_words_list)
        
        return reversed_string



# Write a Python class that has two methods: get_String and print_String , 
#   get_String accept a string from the user and 
#   print_String prints the string in upper case
class Python:
    def __init__(self):
        self.input_string = " "

    def get_String(self):
        input_string = input("enter a string: ")
    
    def print_String (self):
        print(self.input_string.upper())
