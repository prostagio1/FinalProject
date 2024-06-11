import csv
from functions import *
from datetime import datetime

class Customer:
    def __init__(self,filename = "customers.csv",):
        self.customers = filename

    #Adding customers to the customer database
    def add_customer(self,first_name,last_name,email,phone_number):
        customer = [unique_id("customers.csv"),first_name,last_name,email,phone_number]
        with open(self.customers, "a",newline = '') as file:
            writer = csv.writer(file)
            writer.writerow(customer)
    
    #in case of a typo or other kind of mistake, edit can be used.
    def edit_customer(self, customer_id, first_name, last_name, email, phone):
        rows = []
        with open("customers.csv", mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] == customer_id:
                    # Update the information of the product
                    row[1] = first_name
                    row[2] = last_name
                    row[3] = email
                    row[4] = phone
                rows.append(row)

        with open("customers.csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
    
    #user can obtain customer info (name, email,...)
    def get_customer(self, customer_id):
        with open("customers.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == customer_id:
                    display_customer_info(row)


class Product:
    def __init__(self,filename = "products.csv",):
        self.products = filename

    def add_product(self,product_name,description,price):
        product = [unique_id("products.csv"),product_name,description,price]
        with open("products.csv", "a",newline='') as file:
            writer = csv.writer(file)
            writer.writerow(product)
     
    #edits product
    def edit_product(self, product_id, new_product_name, new_description, new_price):
        rows = []
        with open("products.csv", mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] == product_id:
                    # Update the information of the product
                    row[1] = new_product_name
                    row[2] = new_description
                    row[3] = new_price
                rows.append(row)

        with open("products.csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
    def get_product(self, product_id):
        with open("products.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == product_id:
                    display_product_info(row)


class Transaction:
    def __init__(self,filename = "transactions.csv",):
        self.products = filename

    def add_transaction(self,customer_key,product_key,total_quantity):
        transaction = [unique_id("transactions.csv"),customer_key,product_key,total_quantity,get_price(product_key)*float(total_quantity),datetime.today()]
        with open("transactions.csv","a",newline = "") as file:
            writer = csv.writer(file)
            writer.writerow(transaction)
    
    def delete_transaction(self, transaction_id):
        transactions = []
        with open("transactions.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if int(row[0]) != transaction_id:
                    transactions.append(row)
    def edit_transaction(self, transaction_id, customer_key=None, product_key=None, total_quantity=None):
        transactions = []
        with open("transactions.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == transaction_id:
                    if customer_key is not None:
                        row[1] = customer_key
                    if product_key is not None:
                        row[2] = product_key
                    if total_quantity is not None:
                        row[3] = total_quantity
                    row[4] = get_price(row[2]) * int(row[3])
                transactions.append(row)

        with open("transactions.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(transactions)


        with open("transactions.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(transactions)
        






