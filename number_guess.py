import random

random_number = random.randint(0, 20)

# print(random_number)
user_guess = int(input("Enter a number: "))

if random_number > int(user_guess):
    print("Its too low!")
elif random_number < int(user_guess):
    print("It's too high!")
else:
    print("Its the currect number")
