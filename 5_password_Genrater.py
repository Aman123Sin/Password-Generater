import random
latters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbol = ['!','@','#','$','%','&','*']

num_Symbol = int(input("How many symbol would you like in your password: "))
num_latters = int(input("How many latter would you like in your password: "))
num_numbers = int(input("How many number would you like in your password: "))

password = " "

for pas in range(1, num_Symbol + 1):
    password += random.choice(symbol)

for pas in range(1, num_latters + 1):
    password += random.choice(latters)

for pas in range(1, num_numbers + 1):
    password += random.choice(numbers)


print(f"\nYour Password: {password}")