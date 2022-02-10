import connect
import getpass # getpass is already included in base python module ,so no need to install it thorugh pip 

# module for registering employes into the database
def sign():
    print("Create login")
    # take inputes
    id = int(input("Enter Employ_id : "))
    name = input("Enter name :")
    # use getpass for password to hide password 
    password = getpass.getpass('Enter password : ') 
    # get role
    role = input("Enter E to create employ login or Enter M to create Manager login : ")
    #cheak if role is for employ or manager
    if role.lower() == 'e':
        role = 'Employ'
    else:
        role = 'Manager'    
    # register login credentials in database     
    res = connect.signin(id, name, password, role)
    print(res)
    return 0

def main():
    # print menu
    help = '''
    Enter Signup to create new login account.
    Enter ShowStock to Show stock database.
    Enter ShowLogin to Display Login credentials. 
    Enter sale to show Sale Table.
    Enter Help to see this tect again.
    '''
    print(help)
    # get continous input while true
    while True:
        init = input(':-> ')
        if init.lower() == 'signup':
            sign()
        elif init.lower() == 'showstock':
            connect.show_db()  
        elif init.lower() == 'showlogin':
            connect.show_login()
        elif init.lower() == 'sale':
            connect.show_sale()     
        elif init.lower() == 'help':
            print(help) 
        elif init.lower() == 'close':
            break                
        else:
            print('Input error, Try again')    

if __name__ == '__main__':
    main()               
