import connect

def main():
    # print menu
    menu = '''
    Enter showStock to display stock table.
    Enter sale to show sale table.
    Enter Sell to make transition.
    Enter help to see the menu.
    Enter close to close the program.
    '''
    print(menu)
    while True:
        init = input(':-> ')
        if init.lower() == 'sell':
            connect.sell()
        elif init.lower() == 'close':
            break
        elif init.lower() == 'showstock':
            connect.show_db()  
        elif init.lower() == 'help':
            print(menu) 
        elif init.lower() == 'showlogin':
            connect.show_login()
        elif init.lower() == 'sale':
            connect.show_sale()    
        else:
            print('Input error, Try again')   
