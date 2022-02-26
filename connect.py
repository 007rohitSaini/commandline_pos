from datetime import datetime
import mysql.connector
import getpass
import random


# connect to database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",  # database username
    password="saini",  # database password
    database="project"  # database name
)

# define function for MySql Cursor


def cursor():
    cursor = mydb.cursor()
    return cursor


# Run cursor to run with in the program
cur = cursor()

# define funtion for commit


def commit():
    mydb.commit()
    return 0

# Define function for Login


def login():
    # take credentials as input
    name = input("Enter Employ_code:")
    password = getpass.getpass('Enter password: ')
    # fetch user data from databse
    cur.execute(
        "SELECT * FROM login WHERE Employ_code = %s AND Password = %s", (name, password,))
    acc = cur.fetchone()
    if acc:
        return acc  # if account existes return account data
    else:
        login()
        return "Login failed"  # if no account was found then return failes massage


# define function for signing up
def signin(id, name, password, role):
    # cheack if Employ code allready exixts
    cur.execute("SELECT * FROM login WHERE Employ_code = %s", (id,))
    acc = cur.fetchone()

    if acc:
        msg = "Account already exists!"
    else:
        # else resister user
        cur.execute("INSERT INTO login VALUES (%s, %s, %s, %s)",
                    (id, name, password, role))
        commit()
        msg = "Registered Successfully"
        cur.execute("SELECT * FROM login WHERE Employ_code = %s", (id,))
        acc = cur.fetchone()
        print(acc)

    return msg

# module for registering employes into the database


def sign():
    print("Create login")
    # take inputes
    id = int(input("Enter Employ_id : "))
    name = input("Enter name :")
    # use getpass for password to hide password
    password = getpass.getpass('Enter password : ')
    # get role
    role = input(
        "Enter E to create employ login or Enter M to create Manager login : ")
    # cheak if role is for employ or manager
    if role.lower() == 'e':
        role = 'Employ'
    else:
        role = 'Manager'
    # register login credentials in database
    res = signin(id, name, password, role)
    print(res)
    return 0

# Define function to display stock table


def show_db():
    cur.execute("Select * from stock")
    result = cur.fetchall()
    commit()
    if result:
        for row in result:
            print(row, '\n')
    else:
        print("No record found")

# define function to display login table


def show_login():
    cur.execute("Select * from login")
    result = cur.fetchall()
    commit()
    if result:
        for row in result:
            print(row, '\n')
    else:
        print("No record found")

# define function to display Sale table


def show_sale():
    cur.execute("Select * from sale")
    result = cur.fetchall()
    commit()
    if result:
        for row in result:
            print(row, '\n')
    else:
        print("No record found")

# define function to make trancition


def sell():
    res = input("Enter item code to search:")
    cur.execute("Select * from stock WHERE itemcode = %s", (res,))
    item = cur.fetchone()
    if item:
        print(item)
        respo = input("Enter y or n to continue with item fetched : ")
        if respo.lower() == 'y':
            invoice_number = random.randint(1, 1000)
            item_code = item[0]
            item_name = item[1]
            qty = int(input('Enter Quantity of item bought: '))
            name = input("Enter Buyer name: ")
            price = item[3]
            total = price * qty
            date = datetime.now()
            date = date.strftime('%Y-%m-%d %H:%M:%S')

            cur.execute('INSERT INTO sale VALUES (%s,%s, %s, %s, %s, %s, %s, %s)',
                        (invoice_number, item_code, item_name, qty, name, price, total, date))
            commit()

            remain = int(item[2]) - qty

            cur.execute(
                'UPDATE stock SET Quantity = %s WHERE itemcode = %s', (remain, item_code))
            commit()

            print("Thank you for buying Mr./Ms. {} your total is {} for {} units of {}".format(
                name, total, qty, item_name))
        else:
            print("Try another item code or cheak via printing stock table")
            sell()
    else:
        print("Item not found")


def update_Stock():
    what = input(
        "Enter 'new' to enter new item\nEnter 'update' to update existing item\nEnter 'delete' a item from stock.\n-> ")

    if what.lower() == 'new':
        item_code = int(input("Enter Item Code: "))
        name = input("Enter Item Name: ")
        price = int(input("Enter Price: "))
        qty = int(input("Enter quantity aviabale: "))

        cur.execute("INSERT INTO stock VALUES (%s, %s, %s, %s)",
                    (item_code, name, qty, price))
        commit()

        print("item added succesfully")

    elif what.lower() == 'update':
        item_code = int(input("Enter item code to be edited: "))
        stock = int(input("Enter number units currently available: "))
        price = int(input("Enter current price: "))

        cur.execute("UPDATE stock SET Quantity = %s, Price = %s WHERE Itemcode = %s",
                    (stock, price, item_code))
        commit()

        print("Item updated succesfully")

    elif what.lower() == 'delete':
        item_code = int(input("Enter item code to be edited: "))
        cur.execute(
            'select * from stock where Itemcode = %s', (item_code,))

        res = cur.fetchone()

        if res:
            confirm = input(
                "Do you really want to delete {} <Y/N>: ".format(res))
            if confirm.lower() == 'y':
                cur.execute(
                    "DELETE FROM stock WHERE Itemcode = %s", (item_code,))
                commit()
                print('{} successfully removed from database.'.format(res))
            else:
                print('Deletion Error')
        else:
            print("No record found")

    else:
        print("Invalid input")

