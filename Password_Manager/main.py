from sql import find_users, store_password, delet_password
from sql2 import check_password, store_password2, check_email

def login():
    email = input("Enter Your email: ")
    password = input("Enter your password: ")
    retrived_email = check_password(password)
    email_check = check_email(email)
    if retrived_email is None:
        if email_check is not None:
            print("invalid password")
        else:
            print("the account does not exists")
            choice = input("would you like to make an account ? (y/n): ")
            if choice == "y":
                make_account()
            else:
                pass    
    else :
        print("log-ined")
        pass_mang(retrived_email)

def make_account():
    email = input("Enter your email: ")
    password = input("Enter your Master-Password: ")
    confirm = input("Confirm your Master-Password: ")
    if password == confirm:
        store_password2(email,password)
    else:
        print("Both passwords do not match!")    

def pass_mang(email):
    choice = input("Do you want to store password (1) or see your passwords (2)  or delet a password (3): ")
    if choice == "1":
        email = input("Enter your Email: ")
        password = input("Enter your Password: ")
        username = input("Enter your Username: ")
        url = input("Enter the URL: ")
        app_name = input("Enter the app name: ")
        store_password(password,email,username,url,app_name)
    elif choice == "2":
        if email is not None:
            find_users(email)
    elif choice == "3":
        passw = input("Enter the password: ")
        appn = input("Enter the app name: ")
        delet_password(passw,appn)
                        

login()            