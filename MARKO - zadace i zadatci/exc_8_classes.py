# Write a Python class Employee with 
#     attributes like emp_id, emp_name, emp_salary, and emp_department and 
#     methods like calculate_emp_salary, emp_assign_department, and print_employee_details

# Sample Employee Data:
# "ADAMS", "E7876", 50000, "ACCOUNTING"
# "JONES", "E7499", 45000, "RESEARCH"
# "MARTIN", "E7900", 50000, "SALES"
# "SMITH", "E7698", 55000, "OPERATIONS"

# Use 'assign_department' method to change the department of an employee.
# Use 'print_employee_details' method to print the details of an employee.
# Use 'calculate_emp_salary' method takes two arguments: hours_worked,

# which is the number of hours worked by the employee. If the number of hours worked is more than 50, the method computes overtime and adds it to the salary. 
# Overtime is calculated as following formula:

# overtime = hours_worked - 50
# Overtime amount = (overtime * (salary / 50))

class Employee:
    def __init__(self, id, name, salary, department):
      self.id = id
      self.name = name
      self.salary = salary
      self.department = department
    
    def calculate_emp_salary(self, hours_worked):
      overtime_amount = 0

      if hours_worked > 50:
        overtime = hours_worked - 50
        overtime_amount = (overtime * (self.salary / 50))
      
      self.salary = self.salary + overtime_amount

    def emp_assign_department(self, new_department):
      self.department = new_department

    def __str__(self):
      return f"{self.name} - {self.department} - {self.salary}"

employee1 = Employee("E7876", "ADAMS", 50000, "IT")
employee2 = Employee("E7499", "JONES", 45000, "RESEARCH")
employee3 = Employee("E7900", "MARTIN", 50000, "SALES")
employee4 = Employee("E7698", "SMITH", 55000, "OPERATIONS")

print(employee1)
employee1.emp_assign_department("FINANCIJE")
print(employee1)

employee1.calculate_emp_salary(50)
print(employee1)



# Write a Python class Restaurant with 
# attributes like menu_items, book_table, and customer_orders, and 
# methods like add_item_to_menu, book_tables, and customer_order. 
# Perform the following tasks now:
    # Now add items to the menu. +
    # Make table reservations.   +
    # Take customer orders.         -> Za igru, napraviti class Order, koja ima atribute po zelji za order
    # Print the menu.            +
    # Print table reservations.  +
    # Print customer orders.

class Order:
    def __init__(self, food, drink):
        self.food = food
        self.drink = drink


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Restaurant:
    def __init__(self):
        self.menu_items = []
        self.book_table = []
        self.customer_orders = []
    
    def add_item_to_menu(self, name, price):
        item = Item(name, price)
        # item = { "name": name, "price": price }
        self.menu_items.append(item)

    def print_menu_items(self):
        print("Menu items")
        for item in self.menu_items:
            # print(item["name"] + ": " + str(item["price"]) + " price")
            print(f"{item.name}: {item.price} price")

    def book_tables(self, table_id):
        self.book_table.append(table_id)

    def print_book_tables(self):
        print("\nTables")
        for item in self.book_table:
            print(f"Table: {item}")

    def customer_order(self, table_id, order, food, drink):
        order = Order(food, drink)
        order_details = { "table_id": table_id, "order": order }
        self.customer_orders.append(order_details)
    
    def print_customer_orders(self):
       print("Customer orders")
       for customer_order in self.customer_orders:
          table_id = customer_order["table_id"]
          order = customer_order ["order"]
          print(f"Table {table_id} {order.food} {order.drink}")
       

restaurant = Restaurant()

restaurant.add_item_to_menu("Hamburger", 10)
restaurant.print_menu_items()

# Menu items
# Hamburger: 10 price

# Tables
# Table: 1
# Table: 2
# Table: 3

restaurant.book_tables(1)
restaurant.book_tables(2)
restaurant.book_tables(3)

restaurant.print_book_tables()


# Write a Python class BankAccount with attributes like account_number, balance, date_of_opening and customer_name, 
# and methods like deposit, withdraw, and check_balance

class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name


    def deposit(self, amount):
        
        if amount <=0:
            return "Invalid deposit amount"
        else:
            self.balance += amount    
            return "Valid deposit"

    def withdraw(self, amount): 
       if amount > self.balance:      
           return "not enough money"
       else:
           self.balance -= amount
           return "successful withdraw"
           
    def check_balance(self):
       return self.balance

# Write a Python class Inventory with 
  # attributes like item_id, item_name, stock_count, and price, and 
  # methods like add_item, update_item, and check_item_details.
class Item:
    def __init__(self, name, stock_count, price):
        self.name = name
        self.stock_count = stock_count
        self.price = price

class Inventory:
    def __init__(self):
        self.item =  []
        self.item_id_next = 1
       

    def add_item(self, name, stock_count, price):
        item_id = self.item_id_next  # uzimamo id za novi item iz svojstva 'item_id_next'
        item = Item(name, stock_count, price)  # stvaramo novi objekt klase 'Item' s zadanim atributima
        self.items.append({"item_id": item_id, "item": item})  # dodajemo novi objekt klase 'Item' u listu svojstva 'items' zajedno s pripadajućim 'item_id'
        self.item_id_next += 1  # povećavamo 'item_id_next' za 1 kako bi bili sigurni da će se sljedeći 'item' dodati s novim id-om
        return item_id  # vraćamo id novog item-a

    def update_item(self, item_id, name=None, stock_count=None, price=None):
        # Pronalazimo item s odgovarajućim ID-om u listi
        item_to_update = next((item for item in self.items if item['item_id'] == item_id), None) 
        # Pronalazimo item u listi self.items koji ima zadani item_id i sprema ga u varijablu item_to_update. 
        # Ako item s traženim ID-om ne postoji, vrijednost None se dodjeljuje item_to_update
        if item_to_update: # Provjeravamo je li item pronađen u prethodnom koraku
            # Ako postoji item s traženim ID-om, ažuriramo njegove atribute
            if name:
                item_to_update['item'].name = name
            if stock_count:
                item_to_update['item'].stock_count = stock_count
            if price:
                item_to_update['item'].price = price
            return True  # Vraćamo True da potvrdimo da je item uspješno ažuriran
        else:
            return False  # Vraćamo False jer item s traženim ID-om nije pronađen u listi

    def check_item_details(self, item_id):
        item = self.item_details.get(item_id)
        if item:
            print(f"Item ID: {item_id}")
            print(f"Item name: {item['item_name']}")
            print(f"Item stock count: {item['stock_count']}")
            print(f"Item price: {item['price']} USD")
        else:
            print(f"No item found with ID {item_id}")



# Use a dictionary to store the item details, where the key is the item_id 
# and the value is a dictionary containing the item_name, stock_count, and price

    item_details = {
        "item_id_1": {
            "item_name": "Product A",
            "stock_count": 10,
            "price": 19.99
        }
    }
