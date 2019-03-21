#initialise a dictionary
dict = {'1':'1','username':'password'} 
username = input('Enter the username: ')

#fucntion to check the login
def login(username):
    if username in dict:
        password = input('Enter your password: ')
        passwords = dict.values()
        if password in passwords:
            print('Login Succesfull')
            access()
        else:
            print('Invalid password')
    else:
        print('Invalid Username')
    return     
        
#fucntion to give the access to the file after login successfull        
def access():
    opening = open('Secrets.txt')
    line = int(input('Which secret you wanna know? '))
    secretlist = opening.readlines()
    for i in range(len(secretlist)):
        if line == i:
            print(secretlist[i])
    add = input('Do you wanna add a secret? \n Y to yes N to no: ')
    if add in ['Y','y']:
        addsecret()
    else:
        print('No problemo')
    opening.close()   
    
#add content to file    
def addsecret():
    file = open('Secrets.txt', 'a')
    writesecret = input('What do you wanna add? \n Write here: ')
    file.write('\n' +writesecret)
    file.close()  
    
login(username)        