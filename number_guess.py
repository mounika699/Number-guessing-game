import random
def number_guessing_game():
    print('welcome to the number guessing game!')
    print("i'm thinking of a number between 1 and 100")
#genarate a random number between 1 and 100
secret_number=random.randint(1,100)
attempts=0
while True:
    try:
        guess=int(input('enter your guess:'))
        attempts+=1
        if guess<secret_number:
            print("low!try again")
        elif guess >secret_number:
            print('high!try again')
        else:
            print(f"congratulations! you guessed the number{secret_number}in {attempts}attempts")
            break
    except ValueError:
        print('please enter a valid number')

