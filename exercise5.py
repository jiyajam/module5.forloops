######1

import random
number_of_dices= int(input("How many dices?: "))
sum=0
for x in range(number_of_dices):
    roll= (random.randint(1,6))
    sum = sum + roll
print(f"the sum of {number_of_dices} dices is {sum}")

###########2

numbers = []

while True:
    user_input = input("Enter a number (or press Enter to stop): ")
    if user_input == "":
        break
    else:
        numbers.append(int(user_input))


numbers.sort(reverse=True)


print("The five greatest numbers are:", numbers[:5])
#print(help(numbers)) #just wanted to test it out

##################3
integer_number = int(input("Enter any integer : "))
if integer_number > 1 :
    for i in range(2,integer_number):
        if integer_number % i == 0:
            print(f"{integer_number} is not a prime number")
            break
    else:
        print(f"{integer_number} is a prime number")
else:
    print(f"{integer_number} is not a prime number")

################4
cities = []
for x in range(1,6):
    user_input = input(f"enter the name of city {x}: ")
    cities.append(user_input)
for user_input in cities:
    print(user_input)





