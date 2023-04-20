# Create a class Person that can store a persons name (str) and and age (int).
# Instance three persons with the following attributes:

# Dianne (31)
# Sean (27)
# Nathan (34)

# Add a method `print_age()` that prints message in format "{name} is {age} years old". Use it to show that for each instance it prints the message.
# Add a method `add_year()` that increases number of years by one.

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def print_age(self):
        print(f"{self.name} is {self.age} years old")

    def add_year(self):
        self.age += 1

person1 = Person("Dianne", 31)
person2 = Person("Sean", 27)
person3 = Person("Nathan", 34)

person1.print_age()  
person2.print_age() 
person3.print_age()  

person1.add_year()
person1.print_age() 

person2.add_year()
person2.print_age()

person3.add_year()
person3.print_age()



# Create a class Receipt that contains following data:

# * `receipt_id` (str)
# * `total_cost` (float)
# * `items` (list)

# In `items` list there should be names of the product.

# Create following instances:

# * Receipt 1: 
#   - id: 1
#   - total: 10.99
#   - items: bread, milk, cookies
# * Receipt 2: 
#   - id: 2
#   - total: 13.45
#   - items: cat food, cat sand, bowl

class Receipt:
    def __init__(self, receipt_id: str, total_cost: float, items: list):
        self.receipt_id = receipt_id
        self.total_cost = total_cost
        self.items = items


receipt1 = Receipt(receipt_id="1", total_cost=10.99, items=["bread", "milk", "cookies"])
receipt2 = Receipt(receipt_id="2", total_cost=13.45, items=["cat food", "cat sand", "bowl"])

print(f"Total cost is: {receipt2.total_cost}, items: {receipt2.items}")



# Create a TableGame class that contains the following data:

# heading (str)
# id (int)
# name (str)
# min_age (int)
# When heading data changes, it should be changed in all instances.

# Create following instances in a list:

# id=1, name=Monopoly, min_age=3
# id=2, name=Ludo, min_age=8
# id=3, name=Axis & Allies, min_age=12
# Then, in a loop print all instances.

# Add `__str__()` method that returns string representation of an object, like "{heading} ({id}): {name}, minimum age {min_age}".

class TableGame:
    def __init__(self, heading: str, id: int, name: str, min_age: int):
        self.heading = heading
        self.id = id
        self.name = name
        self.min_age = min_age



    def __str__(self):
        return f"{self.heading} ({self.id}): {self.name}, minimum age {self.min_age}"

games = [
    TableGame(heading="game1", id=1, name="Monopoly", min_age=3),
    TableGame(heading="game2", id=2, name="Ludo", min_age=8),
    TableGame(heading="game3", id=3, name="Axis & Allies", min_age=12)
]

for game in games:
    print(game)



# Write a class that can store employee data:
# - name
# - last name
# - title
# - age

# Implement string representation method that is used when printing an object; it should print title, name, last name and age.

# Instance one object and print it.

class EmployeeData:
    def __init__(self, name: str, last_name: str, title: str, age: int):
        self.name = name
        self.last_name = last_name
        self.title = title
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.last_name}): {self.title}, age {self.age}"
    
person01 = EmployeeData("Ivanka", "Budimir", "Mrs", 48)
print(person01)


# Write a class TextPad that has following members:

# * text message with name `message`
# * function `modify(c)` that uses c to pad string with character `c`; if message is *text* and c is `+`, it will be modified to `t+e+x+t`

# Show that the class functions correctly.

class TextPad:
    def __init__(self, message):
        self.message = message
    
    def modify(self, c):
        self.message = self.message.replace("text", f"t{c}e{c}x{c}t")

# Create class HouseholdBill with the following attributes:
# * bill type (e.g. electric, water, phone, tv)
# * amount (float)
# * paid (bool)

# The bill must be always instanced as not paid.

# Create method `set_paid(paid)` that modifies the `paid` flag to the passed boolean value.

# Create 3 bills in a list, set first one as paid and in a loop print bills that are not paid.

class HouseholdBill:
    def __init__(self, bill_type, amount):
        self.bill_type = bill_type
        self.amount = amount
        self.paid = False

    def set_paid(self, paid):
        self.paid = paid

bill1 = HouseholdBill("electric", 3.50)
bill2 = HouseholdBill("water", 5.50)
bill3 = HouseholdBill("phone", 7.30)

bill1.set_paid(True)

bills = [bill1, bill2, bill3]

for bill in bills:
    if not bill.paid:
        print(f"{bill.bill_type}: {bill.amount}")
