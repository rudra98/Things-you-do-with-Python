#import necessary modules
import sys
#definition of the fucntion for adding extra content to the file
def add(user_input):
    #opening the file
    writing = open('file.txt', 'a')
    #input from user to add to file
    adding = input('Do you want to answer this question? Y to yes, N to no: ')
    if adding in ('Y', 'y'):
            answer = input('Answer: ')
            wholeans = (user_input+':'+answer)       
            writing.write('\n'+wholeans)
            writing.close()
    else:
            print('No problemo')
            sys.exit()

#From here we start the first step of program 
print("\nAsk a question or just type 'quit' to end the program")
while True:
    #user input is taken in lower case
    user_input = input('Ask me anything: ').lower()
    #loading our file
    biglist = open('file.txt', 'r').readlines()
    
    if user_input in ('quit'):
        sys.exit()    
        
    #initialising an empty list  
    new = []
    for n in range(len(biglist)):
        #here we spilt the file in different sections by ':' 
        bigsplit = biglist[n].split(':')
        
        #As we cant keep adding in a loop, thus we extend the list
        new.extend(bigsplit)
        
        
    #to check the input in file    
    if user_input not in new:
        add(user_input)  
    for n in range(len(biglist)):
        splitlist = biglist[n].split(':')
        if user_input == splitlist[0]:
            print(splitlist[1])
            break
        else:
            continue
    continue   
    



    

            