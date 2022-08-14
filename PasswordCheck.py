#This is a password check, it checks for diffrent parameters of a password and helps you get a perfectly safe password.
#Those parameters are:
#1) needs atleast 1 lowercase letter
#2) needs atleast 1 uppercase letter
#3) needs atleast 1 special character
#4) needs atleast 1 number
#5) needs to have more than 8 characters
import string
low = 'no'
up = 'no'
num = 'no'
char = 'no'
sum=0
#assigning each array
lowercase=list(string.ascii_lowercase)
uppercase=list(string.ascii_uppercase)
symbols = ['`', '~', '!', '@', '#','$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '[', '}', '}', '|', "/", ':', ';', '<', ',', '>', '.', '?', '/', '"', "'"]
number = ['1','2','3','4','5','6','7','8','9','0']
word=str(input('Enter your password: '))
length=len(word)
#the whole checking process will only happen in the entered pswd has more than 8 characters in it
if length>=8:
    for i in range (0,length):
#checking for lowercase letters
        for o in range (0,26):
            sum1=length-1
            sum2=sum1-i
            sum3=0-sum2
            if i != length-1:
                if word[i:sum3] == lowercase[o]:
                    low='yes'
            if i == length-1:
                if word[i:] == lowercase[o]:
                    low='yes'
#checking for uppercase letters
        for p in range (0,26):
            sum1=length-1
            sum2=sum1-i
            sum3=0-sum2
            if i != length-1:
                if word[i:sum3] == uppercase[p]:
                    up='yes'
            if i == length-1:
                if word[i:] == uppercase[p]:
                    up='yes'
#checking for special characters
        for a in range (0,32):
            sum1=length-1
            sum2=sum1-i
            sum3=0-sum2
            if i != length-1:
                if word[i:sum3] == symbols[a]:
                    char='yes'
            if i == length-1:
                if word[i:] == symbols[a]:
                    char='yes'
#checking for numbers
        for s in range (0,9):
            sum1=length-1
            sum2=sum1-i
            sum3=0-sum2
            if i != length-1:
                if word[i:sum3] == number[s]:
                    num='yes'
            if i == length-1:
                if word[i:] == number[s]:
                    num='yes'
#finalising if there are lowercase letters
    if low == 'yes':
        sum=sum+1
    elif low == 'no':
        print('The password must contain atleast 1 lowercase letter')
#finalising if there uppercase letters  
    if up == 'yes':
        sum=sum+1
    elif up == 'no':
        print('The password must contain atleast 1 uppercase letter')
#finalising if there special characters    
    if char == 'yes':
        sum=sum+1
    elif char == 'no':
        print('The password must contain atleast 1 special character')
#finalising if there are numbers
    if num == 'yes':
        sum=sum+1
    elif num == 'no':
        print('The password must contain atleast 1 number')
        
else:
    print('The password must contain atleast 8 or more characters')
    
if sum == 4:
    print("You've got yourself a perfect password!")
    print('Thank You!!')
