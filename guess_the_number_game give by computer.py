import random

def user_guess(x):
    random_number = random.randint(1,x)
    guess=0
    while guess != random_number:
        guess=int(input(f"guess the number between 1 and {x}"))
        if guess == random_number :
            print("congrats. you have guessed the number",random_number,"correctly!!")
            print(f"congrats. you have guessed the number {random_number} correctly!!")
            break
        if guess < random_number :
            print("the guess is to low")
        else :
            print("the guess is to high")
            
    
user_guess(10)
