#taking user input in lower case
user_input = input('What do you wanna search?: ').lower()

#loading the file in the program
#.readlines to store to text in op
op = open('C:/Users/saura/Desktop/para.txt').readlines()

#' '.join to join the op variable's content
op  = ' '.join(op)

#replace newline with space
op = op.replace('\n','').lower() 
    
found = 0
#check if the user input is in the file or not
if user_input in op:
    found = 1
if found == 1:
    print('Yes it is in the text file')
else:
    print('No it is not in the file')
       