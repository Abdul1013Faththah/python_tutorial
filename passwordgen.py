import random

chars='qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM!@#$%&'

number_of_charcter=int(input("Enter the the lenght of the password : "))

password=''
for i in range(number_of_charcter):
    password= password + random.choice(chars)

print(password)
    
