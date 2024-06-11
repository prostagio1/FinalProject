import csv

abc = "abcdefghijklmnopqrstuvwxyz"
ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
numbers = "0123456789"


def is_string(text):
    for i in text:
        if (i in special_characters) or (i in numbers):
            return False
    return True

def is_phone_number(phone_number):
    valid = True
    for i in phone_number:
        if (i in abc or i in ABC or i in special_characters):
            valid = False
    if len(phone_number) != 9:
        valid = False
    if not phone_number.startswith("5"):
        valid = False   
    return valid

def is_valid_email(email):
    if "@" in email and "." in email:
        if email.index("@") < email.index("."):
            return True
    return False



def menu():
    print("1. Register New Customer! ")
    print("2. Edit Customer! ")
    print("3. Get Customer Information! ")
    print("4. Add Product! ")
    print("5. Edit Product! ")
    print("6. Add Transaction! ")
    print("7. Edit Transaction! ")
    print("8. Aggregate by Customer!  ")
    print("9. Aggregate by Product!  ")
    print("10. Get Product Information!  ")

    print("0. Quit! ")



def unique_id(filename):
    try:
        with open(filename,"r") as file:
            reader = csv.reader(file)
            last_row = None
            for row in reader:
                last_row = row
            return int(last_row[0]) + 1

    except TypeError:
        return 1

#checks weather customer exists in customers database
def customer_exists(id):
    exists = False
    with open("customers.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == id:
                exists = True
    return exists

def product_exists(id):
    exists = False
    with open("products.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == id:
                exists = True
    return exists

def transaction_exists(id):
    exists = False
    with open("transactions.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == id:
                exists = True
    return exists


def get_price(id):
    with open("products.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == id:
                return float(row[3])
            
def display_customer_info(row):
    print(f"ID: {row[0]}")
    print(f"First_Name: {row[1]}")
    print(f"Last_Name: {row[2]}")
    print(f"E-Mail: {row[3]}")
    print(f"PHONE: {row[4]}")


def display_product_info(row):
    print(f"ID: {row[0]}")
    print(f"Name: {row[1]}")
    print(f"Desc: {row[2]}")
    print(f"Price {row[3]}")


            
print(get_price("1"))


def sum_of_sales_by_customer(id):
    sum = 0
    with open('transactions.csv', 'r', newline='') as file:
        reader = csv.reader(file)
    
    # Iterate over each row
        for row in reader:
            if row[0] == id:
                sum += float(row[4])

    return sum


def sum_of_sales_by_product(id):
    sum = 0
    with open('transactions.csv', 'r', newline='') as file:
        reader = csv.reader(file)
    
    # Iterate over each row
        for row in reader:
            if row[1] == id:
                sum += float(row[4])

    return sum
 
            
            




    
        

