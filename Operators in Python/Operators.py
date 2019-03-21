#display the menu
while True:
    
    print("""
          Hey there
          What you wanna do?
          """)
    print("Enter 'add' to add two numbers: ")
    print("Enter 'sub' to subtract two numbers: ")
    print("Enter 'mul' to multiply two numbers: ")
    print("Enter 'div' to divide two numbers: ")
    print("Enter 'mod' to take out modulo: ")
    print("Enter 'pow' to do exponentiation: ")
    print("Enter 'quit' to end the program: ")
    user_input = input()
    
    if user_input == 'quit':
        break

#take the numbers from user    
    var1 = float(input('Enter 1st number: '))
    var2 = float(input('Enter 2nd number: '))

#operations to be performed    
    if user_input == 'add':
        if user_input == 'add':
            res = var1 + var2
            print('The result is ',res)
        elif user_input == 'sub':
            if var1 > var2:
                res = var1 - var2
                print('The result is ',res)
            else:
                print('Somethings wrong')
        elif user_input == 'mul':
            res = var1 * var2
            print('The result is ',res)
        elif user_input == 'div':
            res = var1/var2
            print('The result is ',res)
        elif user_input == 'mod':
            if var1 > var2:
                res = var1%var2
                print('The result is ',res)
            else:
                print('cmon buddy, try again')
        elif user_input == 'pow':
            res = var1**var2
            print('The result is',res)
        else:
            print("You shouldn't be here")
            
    else:
        print('Are you kidding me: ')
    
    more = str(input('Wanna do more, y to yes and n to no: '))
    if more == 'y':
        continue
    else:
        break
        