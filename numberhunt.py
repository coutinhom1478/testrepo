import random
number = random.randint(0,100)
while True:
    try:
        user_Number = input("Insert a number between 1 and 100: ")
        user_Number = int(user_Number)
        if user_Number == number:
            print("You are right, great job!")
            break
        elif user_Number > number:
            print ("Your guess is high, try again!")
        else:
            print ("Your guess is low, try again!")
    except ValueError:
        print("Invalid Input! Please enter a valid number.")
