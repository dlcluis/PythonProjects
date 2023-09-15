#Random Password Generator

import random

uppercase_letters= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters= uppercase_letters.lower()

digits = "0123456789"
symbols = "()[]{},;:.-_/\\?+*#"

upper,lower,nums,syms = True,True,True,True
all=''
if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if digits:
    all+=digits
if symbols:
    all+=symbols

#length of password
# FIX: the length var is not being converted from str to int

length= input("How long would you like the passwords to be ? ")

while length.isdigit() == False:
    print("oops that was not a number try again")
    length= input("How long would you like the passwords to be ? ")
else:
    length = int(length)

amount= input("How many passwords do you need ? ")
while amount.isdigit()== False:
    print("oops that was not a number try again")
    amount= input("How many passwords do you need ? ")
else:
    amount= int(amount)


passwords=[]
for i in range(amount):
    password= "".join(random.sample(all,length))
    passwords.append(password)


for p in passwords:
    z= str(passwords.index(p) + 1)
    print('Password '+ z + ' is: ' + p)

