import random

random_number = random.randint(0, 1000)

# print(random_number)
user_guess = int(input("Enter a number: "))

if random_number != int(user_guess):
    print("Doesn't match")
else:
    print("Congratulations! You've won.")
