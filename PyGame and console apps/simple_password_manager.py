from cryptograghy.fernet import fernet

#creates a random key
'''
def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)
'''
#loads the random key
def load_key():
     file = open('key.key', 'rb')
     key = file.read()
     file.close()
     return key

key = load_key() + master_pwd.encode()
fer = Fernet(key)
#funtion to split the data and used a for loop to retrieve all the lines from the document
def view():
    
    with open('account_info', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split(": ")
            print('Username: ', user, 'Password: ', fer.decrypt(passw.encode()).decode())
#rstrip removes the invisible \n from the file when reading it
#funtion to create/edit a file and add information
def add():
    user_name = input("Username: ")
    pwd = input("Password: ")
                              #a is a mode to modify/create the file
    with open('account_info', 'a') as f:
        f.write(user_name + ': ' + fer.encrypt(pwd.encode().decode()) + "\n")
#while loop to access any of the two funtions, exits when the value is equal to q
while True:
    mode = input("Would you like to add or view existing passwords? (view, add, q to quit) ")
    if mode == 'q':
        break

    if mode == 'add':
        add()

    if mode == 'view':
        view()
