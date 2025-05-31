# add or view password
# ask user to add or view the password
# add in a file
# view from file
# encrypt and dcrypt password


from cryptography.fernet import Fernet
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)

'''
def load_key():
    file = open("key.key","rb")
    key = file.read()      
    file.close()
    return key
    
    
key = load_key()
fer = Fernet(key)

def view():
    with open("passwords.txt",'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("Username: " ,user ,"|", "Password: ",
                  fer.decrypt(passw.encode()).decode())
            #fer.decrypt({passw}.encode()) 
          
        
def add():
    user_name = input("Enter name: ")
    user_pwd = input("Enter passsword: ")
    
    with open('passwords.txt','a')as f:
        f.write(user_name + "|" + fer.encrypt(user_pwd.encode()).decode() + "\n")#fer.encrypt(user_pwd.encode()).decode()
        

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
   
    