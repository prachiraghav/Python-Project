# add or view password
# ask user to add or view the password
# add in a file
# view from file
# encrypt and dcrypt password


from cryptography.fernet import Fernet

master_pwd = input("Enter master password: ")


def view():
    with open("passwords.txt",'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print(f"Username: {user} | Password: {passw}\n")
        
def add():
    user_name = input("Enter name: ")
    user_pwd = input("Enter passsword: ")
    
    with open('passwords.txt','a')as f:
        f.write(user_name + "|" + user_pwd + "\n")
        

while True:
    choice = input("Enter your choice. Add or view or quit: ").lower()
    
    if choice ==  "add":
        add()
    elif choice == "view":
        view()
    elif choice == "quit":
        break
    else:
        print("Invalid Input choose again.")
   
    