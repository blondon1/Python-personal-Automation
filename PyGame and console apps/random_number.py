import random
#there's also randrange(,) but doesnt include the second value
random_n = random.randint(1, 9)
print(random_n)
print('Hello, Wellcome to Guess the random number game')
start = input('Would you like to play?yes or no ').lower()
#stops the program if the user's input isn't yes
if start != 'yes':
    quit()

print("Guess the number!!!")
guess = input('Whats the number? ')

if guess.isdigit():
    guess = int(guess)
elif guess <= 0:
    print('Number has to be larger than 0')
    quit()
else:
    print("You didn't type a number")
    quit()


while random_n != guess:
    print('You got it wrong, try again')
    if guess < random_n:
        print("Too high")
    elif guess > random_n:
        print('too low')
        guess = input('Whats the number? ')
        guess = int(guess)
    else:
        print("Guess what? You won the game!!!")
        print(f"The random number was {random_n}")
        


