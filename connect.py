from datetime import datetime as date
import mysql.connector
import getpass


# connect to database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",# database username
  password="saini" # database password
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
    password = getpass.getpass('Enter password : ')
    # fetch user data from databse 
    cur.execute("SELECT * FROM project.login WHERE Employ_code = %s AND Password = %s", (name, password,))
    acc = cur.fetchone()
    if acc:
        return acc # if account existes return account data
    else:
        return "Login failed" # if no account was found then return failes massage

#define function for signing up 
def signin(id,name,password,role):
    # cheack if Employ code allready exixts
    cur.execute("SELECT * FROM project.login WHERE Employ_code = %s",(id,))
    acc = cur.fetchone()

    if acc:
        msg = "Account already exists!"
    else:
        # else resister user 
        cur.execute("INSERT INTO project.login VALUES (%s, %s, %s, %s)",(id, name, password, role))
        commit()
        msg = "Registered Successfully"
        cur.execute("SELECT * FROM project.login WHERE Employ_code = %s",(id,))
        acc = cur.fetchone()
        print(acc)

    return msg

# Define function to display stock table
def show_db():
    cur.execute("Select * from project.stock") 
    result = cur.fetchall() 
    commit()  
    for row in result:
        print(row, '\n') 

#define function to display login table
def show_login():
    cur.execute("Select * from project.login") 
    result = cur.fetchall() 
    commit()  
    for row in result:
        print(row, '\n') 

#define function to display Sale table
def show_login():
    cur.execute("Select * from project.sale") 
    result = cur.fetchall() 
    commit()  
    for row in result:
        print(row, '\n')  

#define function to make trancition
def sell():
    res = input("Enter item code to search:")
    cur.execute("Select * from project.stock WHERE itemcode = %s",(res,))
    item = cur.fetchone()
    if item:
        print(item)
        respo = input("Enter y or n to continue with item fetched : ")
        if respo.lower() == 'y':
            item_code = item[0]
            item_name = item[1]
            qty = int(input('Enter Quantity of item bought: '))
            name = input("Enter Buyer name: ")
            price = item[3]
            total = price * qty
            datetime = date.now()

            cur.execute('INSERT INTO project.sale VALUES (%s, %s, %s, %s, %s, %s, %s)',(item_code, item_name, qty, name, price, total, datetime))
            commit()

            remain = int(item[2]) - qty    

            cur.execute('UPDATE project.stock SET Quantity = %s WHERE itemcode = %s'),(remain, item_code)
            commit()

            print("Thank you for buying Mr./Ms. {} your total is {} for {} units of {}".format(name, total, qty, item_name))
        else:
            print("Try another item code or cheak via printing stock table")
            sell()
    else:
        print("Item not found")    

def update_Stock():
    what = input("Enter New to enter new item else enter update to update existing item")

    if what.lower() == 'new':
        item_code = int(input("Enter Item Code: "))
        name = input("Enter Item Name: ")
        price = int(input("Enter Price: "))
        qty = int(input("Enter quantity aviabale: "))

        cur.execute("INSERT INTO project.stock VALUES (%s, %s, %s, %s)",(item_code, name, qty, price))
        commit()

        print("item added succesfully")

    else:
        item_code = int(input("Enter item code to be edited: "))
        stock = int(input("Enter number units currently available: "))
        price = int(input("Enter current price: "))

        cur.execute("UPDATE project.stock SET stock = %s, price = %s WHERE itemcode = %s",(stock, price, item_code))
        commit()

        print("Item updated succesfully")
