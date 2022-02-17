import connect
import getpass # getpass is already included in base python module ,so no need to install it thorugh pip 



def main():
    # print menu
    help = '''
    Enter Signup to create new login account.
    Enter ShowStock to Show stock database.
    Enter ShowLogin to Display Login credentials. 
    Enter update to edit stock table.
    Enter sale to show Sale Table.
    Enter Help to see this tect again.
    '''
    print(help)
    # get continous input while true
    while True:
        init = input(':-> ')
        if init.lower() == 'signup':
            connect.sign()
        elif init.lower() == 'showstock':
            connect.show_db()  
        elif init.lower() == 'showlogin':
            connect.show_login()
        elif init.lower() == 'sale':
            connect.show_sale()     
        elif init.lower() == 'update':
            connect.update_Stock()    
        elif init.lower() == 'help':
            print(help) 
        elif init.lower() == 'close':
            break                
        else:
            print('Input error, Try again')    

if __name__ == '__main__':
    main()               
