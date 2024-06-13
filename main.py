from functions import *
from classes import *




def main():
    #Creating the classes
    customers = Customer()
    products = Product()
    transactions = Transaction()
    
    while True:
        menu()
        choice = input("Please enter your choice: ")
        #Option for quitting the application
        if choice == "0":
            exit("Thanks for using our application! <3")
        #Option for registering customer
        elif choice == "1":
            first_name = input("Please enter customers first name: ")
            if is_string(first_name):
                pass
            else:
                print("Invalid First Name")
                continue
            last_name = input("Please enter customers last name: ")
            if is_string(first_name):
                pass
            else:
                print("Invalid Last Name")
                continue
            email = input("Please enter customers email: ")
            if is_valid_email(email):
                pass
            else:
                print("Invalid email")
                continue
            phone = input("Please enter customers Phone Number: ")
            if is_phone_number(phone):
                pass
            else:
                print("Invalid email")
                continue
            customers.add_customer(first_name,last_name,email,phone)
        #Option for editing customer
        elif choice == "2":
            id = input("Please enter customer ID: ")
            if customer_exists(id):
                pass
            else:
                print("Please enter the valid ID!")
                continue
            first_name = input("Please enter customers first name: ")
            if is_string(first_name):
                pass
            else:
                print("Invalid First Name")
                continue
            last_name = input("Please enter customers last name: ")
            if is_string(first_name):
                pass
            else:
                print("Invalid Last Name")
                continue
            email = input("Please enter customers email: ")
            if is_valid_email(email):
                pass
            else:
                print("Invalid email")
                continue
            phone = input("Please enter customers Phone Number: ")
            if is_phone_number(phone):
                pass
            else:
                print("Invalid email")
                continue
            customers.edit_customer(id,first_name,last_name,email,phone)
        #Option for customer info
        elif choice == "3":
            id = input("Please enter customer ID: ")
            if customer_exists(id):
                customers.get_customer(id)
        #Option for registering product
        elif choice == "4":
            product_name = input("Please enter the product name: ")
            if is_string(product_name):
                pass
            else:
                print("Invalid Product Name")
                continue
            desc = input("Please enter the product description: ")
            price = input("Please enter the product price: ")
            try:
                price = float(price)
            except ValueError:
                print("Please enter valid price for the product! ")
                continue
            products.add_product(product_name,desc,price)
        
        #Option for editing product
        elif choice == "5":
            ID = input("Please enter the product ID: ")
            if product_exists(ID):
                product_name = input("Please enter the product name: ")
                if is_string(product_name):
                    pass
                else:
                    print("Invalid Product Name")
                    continue
                desc = input("Please enter the product description: ")
                price = input("Please enter the product price: ")
                try:
                    price = float(price)
                except ValueError:
                    print("Please enter valid price for the product! ")
                    continue
                products.edit_product(ID,product_name,desc,price)
        
        #Option for adding new transaction
        elif choice == "6":
            customer_key = input("Please enter the customer key: ")
            if not customer_exists(customer_key):
                print("Please enter valid customer key! ")
                continue
            product_key = input("Please enter the product key: ")
            if not product_exists(product_key):
                print("Please enter valid product key ")
                continue
            try:
                quantity = float(input("Please enter the quantity: "))
            except ValueError:
                print("Please enter valid quantity! ")
                continue
            transactions.add_transaction(customer_key,product_key,quantity)
        
        #Option for editing transaction
        elif choice == "7":
            tranction_id = input("Please enter the transaction ID: ")
            if not transaction_exists(tranction_id):
                print("Please enter the valid transaction! ")
                continue
            customer_key = input("Please enter the customer key: ")
            if not customer_exists(customer_key):
                print("Please enter valid customer key! ")
                continue
            product_key = input("Please enter the product key: ")
            if not product_exists(product_key):
                print("Please enter valid product key ")
                continue
            try:
                quantity = float(input("Please enter the quantity: "))
            except ValueError:
                print("Please enter valid quantity! ")
                continue
            transactions.edit_transaction(tranction_id,customer_key,product_key,quantity)
        #SUM of the total sales by customer
        elif choice == "8":
            customer_key = input("Please enter the customer key: ")
            if not customer_exists(customer_key):
                print("Please enter valid customer key! ")
                continue
            print(f"Customer with ID {customer_key} has total purchases of {sum_of_sales_by_product(customer_key)}")
        #SUM of the total sales by Product
        elif choice == "9":
            product_key = input("Please enter the Product key: ")
            if not product_exists(product_key):
                print("Please enter valid Product key! ")
                continue
            print(f"Product With ID {product_key} Has Total Sales of {sum_of_sales_by_product(product_key)}")
        #Info about Product
        elif choice == "10":
            product_key = input("Please enter the Product key: ")
            if not product_exists(product_key):
                print("Please enter valid Product key! ")
                continue
            products.get_product(product_key)
        elif choice == "11":
            get_all_customers()
        elif choice == "12":
            get_all_products()
        elif choice == "13":
            get_all_transactions()

if __name__ == "__main__":
    main()
