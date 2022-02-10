import connect
import manager
import employ

def main():
    print('Welocme to Apple.inc ')
    user = connect.login()

    if user == 'Login failed':
        print(user)
    else:
        print('Welcome',(user[1]))
        if user[3]=='Employ':
            employ.main()
        else:
            print(user[1])
            manager.main()    

if __name__ == '__main__':
    main()