# Create class ProgressTracker with the attribute `percent_completed` that is inizially set to `0`.

# Implement method `print_percent_completed()` which prints the value of `percent_completed` variable.

# Implement method `add_percent_completed(value)` which adds the value to `percent_completed` variable.

# Create two progress trackers.
# In a loop, increase 10 times first one by 10, and the second one by loop index.
# After the loop, print `percent_completed` of each tracker.
class ProgressTracker:
    def __init__(self):
        self.percent_completed = 0

    def print_percent_completed(self):
        print(f"Percent completed: {self.percent_completed}")
    
    def add_percent_completed(self, value):
        self.percent_completed += value

progrestracker1 = ProgressTracker()
progrestracker2 = ProgressTracker()

for i in range(1, 11):
    progrestracker1.add_percent_completed(10)
    progrestracker2.add_percent_completed(i)

print("Progress 1:")
progrestracker1.print_percent_completed()

print("Progress 2:")
progrestracker2.print_percent_completed()


# Write a class `TextMod`, which initializes with a string parameter.
# Write a method `print_mirror` that prints that string in reversed and original order of characters, concatenated in one string, divided by a hyphen.
# E.g. for "test" it should print "test-tset".


class TextMod:
    def __init__(self, text):
        self.text = text
    
    def print_mirror(self):
        print(f"{self.text}-{self.text[::-1]}")


# Write a class that manipulates string using following methods:

# * method `mirror(text)` returns mirrored string (mirror -> mirrorrorrim)
# * method `mirror_r(text)` returns reverse mirrored string (mirror -> rorrimmirror)
# * method `sum_ascii(text)` returns sum of ascii values of string characters

class Manipulates:
    def mirror(self, text):
        return text + text[::-1]

    def mirror_r(self, text):
        return text[::-1] + text

    def sum_ascii(self, text):
        total = 0
        for char in text:
            total += ord(char)
        return total
    
m = Manipulates()
text = "mirror"
print(m.mirror(text))    
print(m.mirror_r(text))  
print(m.sum_ascii(text)) 


# Write a class that represents a player in a game.
# Class should initialize with the following data:

# * Name `(name: str)`
# * Life Points `(points: int)`
# * Player speed `(speed: float)`

# It should have the following methods:

# * `apply_damage(amount: int, default is 1)` - lowers Life Points for amount; if it falls under `0`, set it to `0` and print *Game over*
# * `mod_speed(is_faster: bool)` - if `is_faster` is `True`, increase speed by `1`, otherwise decrease it by `1`
# * for a string representation print Name, Life Points and Speed

class Player:
    def __init__(self, name:str,  points:int, speed:float):
        self.name = name
        self.points = points
        self.speed = speed
    
    def apply_damage(self, amount: int = 1):
        self.points -= amount  
        if self.points <= 0:
            self.points = 0
            print ("game over")
    
    def mod_speed(self, is_faster: bool):
        if is_faster:
            self.speed += 1
        else: 
            self.speed -= 1 
    
    def __str__(self):
        return f"{self.name}: {self.points}LP, {self.speed}SP"



# Create a class ComputerMouse.
# Class must have the following attributes:
# - brand (string)
# - model (string)
# - is_bluetooth (bool)
# - weight (int)
# - dpi (int)
# - number_of_buttons (int)
# - free_wheel (bool)

# All fields should be set in a constructor.

# Default values are:
# - is_bluetooth: False
# - free_wheel: False

# Create three instances:
# ```
# pc_mouse1 = ComputerMouse("Logitech", "MX Master 2S", 141, 4000, 8, True, True)
# pc_mouse2 = ComputerMouse("Razer", "DeathAdder", 96, 6400, 5, False, True)
# pc_mouse3 = ComputerMouse("Kensington", "Pro Fit", 204, 2400, 5)
# ```
# Print brand, model and number of DPI for each of them.

class ComputerMouse:
    def __init__(self, brand: str, model: str, weight: int, dpi: int, number_of_buttons: int, is_bluetooth=False, free_wheel=False):
        self.brand = brand
        self.model = model
        self.weight = weight
        self.dpi = dpi
        self.number_of_buttons = number_of_buttons
        self.is_bluetooth = is_bluetooth
        self.free_wheel = free_wheel

pc_mouse1 = ComputerMouse("Logitech", "MX Master 2S", 141, 4000, 8, True, True)
pc_mouse2 = ComputerMouse("Razer", "DeathAdder", 96, 6400, 5, False, True)
pc_mouse3 = ComputerMouse("Kensington", "Pro Fit", 204, 2400, 5)

print(pc_mouse1.model, pc_mouse1.brand, pc_mouse1.dpi)
print(pc_mouse2.model, pc_mouse2.brand, pc_mouse2.dpi)
print(pc_mouse3.model, pc_mouse3.brand, pc_mouse3.dpi)



# Write a class to store information about books (title, author, page count).

# Write the methods:
# - method that prints a book in the format "Book {title} of author {author} has {page count} pages"
# - if the book is over 200 pages, add a note "(thick)" to the printed message

# Load the title, author, and page count values from the user.

class Book:
    def __init__(self, title, author, page_count):
        self.title = title
        self.author = author
        self.page_count = page_count
    
    def print_info(self):
        print(f"Book {self.title} of author {self.author} has {self.page_count} pages", end="")
        if self.page_count > 200:
            print(" (thick)", end="")
        print()

title = input("Enter book title: ")
author = input("Enter author name: ")
page_count = int(input("Enter page count: "))

book1 = Book(title, author, page_count)

book1.print_info()


# Write a class to hold the data about courses. 

# One course has the following data:
# - name
# - number of ECTS point

# Allow the user to load as many courses as they want. Print all of the courses entered with the associated number of ECT points. Calculate the total number of ECTS points.

class Course:
    def __init__(self, name, ECTS):
        self.name = name
        self.ECTS = ECTS
    
    def display(self):
        print(f"{self.name} - {self.ECTS} ECTS")

    
    @staticmethod
    def total_ects(courses):
        total = sum(course.ECTS for course in courses)
        return total

courses = []
while True:
    name = input("Enter the course name (or 'q' to quit): ")
    if name == 'q':
        break
    ECTS = int(input("Enter the number of ECTS points: "))
    course = Course(name, ECTS)
    courses.append(course)

print("Course list:")
for course in courses:
    course.display()

total = Course.total_ects(courses)
print(f"Total ECTS points: {total}")


# Create a class Receipt that holds the following data:

# * `id` (int)
# * `amount` (float)

# Class should automatically set id to the next id in a sequence, which starts in 1.

# Create 3 instances and show that each instance has automatically generated id.


class Receipt:
    next_id = 1

    def __init__(self, amount: float):
        self.id = Receipt.next_id
        Receipt.next_id += 1
        self.amount = amount

receipt1 = Receipt(10.50)
receipt2 = Receipt(20.00)
receipt3 = Receipt(5.75)

print(receipt1.id) 
print(receipt2.id) 
print(receipt3.id) 

# Write a CarOwner class that stores information about the car owner.

# The class contains the following data:
# - name
# - surname
# - address

# Define a dictionary with the license plate as a key, and the value should be CarOwner instance. Allow the user to enter as many license plates and owners as he wants.

# Enable search by registration. If the registration is in the dictionary, print the information about the owner.

class CarOwner:
    def __init__(self, name, surname, address):
        self.name = name
        self.surname = surname
        self.address = address

owners = {}

while True:
    plate_number = input("Enter plate number (or 'q' to quit): ")
    if plate_number == 'q':
        break
    name = input("Enter owner name: ")
    surname = input("Enter owner surname: ")
    address = input("Enter owner address: ")
    owner = CarOwner(name, surname, address)
    owners[plate_number] = owner

search_plate = input("Enter plate number to search: ")
if search_plate in owners:
    owner = owners[search_plate]
    print(f"Owner name: {owner.name}")
    print(f"Owner surname: {owner.surname}")
    print(f"Owner address: {owner.address}")
else:
    print("Registration not found.")
