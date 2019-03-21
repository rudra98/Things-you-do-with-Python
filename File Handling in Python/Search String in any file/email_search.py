#importing re module
import re

#loading the file containing emails
emails = open('emails.txt').readlines()
var2 = []

#checking the input by special symbols using .search fucntion
for string in emails:
    var = re.search("yahoo.com$", string)
    if (var):
        var2.append(string)
    
var3 = len(var2)    

