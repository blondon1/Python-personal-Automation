import random
#imports random library
user_wins = 0
computer_wins = 0
"""
rock < paper , > scissors , = rock


paper > rock , < scissors , = paper


scissors  > paper , < rock , = scissors

checks if the user entered the risght value 
"""
print('Welcome to Rock, Paper, Scissors')
while user_wins < 10 or computer_wins < 10:
    
    

    hand = ['rock', 'paper', 'scissors']
    #sets up the computer 
    random_n = random.randint(0, 2)
    print(random_n)
    bot_hand = hand[random_n]


    #gets the input information with the .lower method
    player_hand = input('Rock, Paper or Scissors? ').lower()
    #if else statement chain to compare imput and random values
    if player_hand == 'rock' and bot_hand == 'scissors':
        print(f"The computer shows {bot_hand}, so you win!!!")
        user_wins += 1
    elif player_hand == 'rock' and bot_hand == 'paper':
        print(f"The computer shows {bot_hand}, so you lost")
        computer_wins += 1
    elif player_hand == 'rock' and bot_hand == 'rock':
        print("It's a tie")
    elif player_hand == 'paper' and bot_hand == 'scissors':
        print(f"The computer shows {bot_hand}, so you lost")
        computer_wins += 1
    elif player_hand == 'paper' and bot_hand == 'rock':
        print(f"The computer shows {bot_hand}, so you win!!!")
        user_wins += 1
    elif player_hand == 'paper' and bot_hand == 'paper':
        print("It's a tie")
    elif player_hand == 'scissors' and bot_hand == 'paper':
        print(f"The computer shows {bot_hand}, so you win!!!")
        user_wins += 1
    elif player_hand == 'scissors' and bot_hand == 'rock':
        print(f"The computer shows {bot_hand}, so you lost")
        computer_wins += 1
    elif player_hand == 'scissors' and bot_hand == 'scissors':
        print("It's a tie")

#final messages
print(f'You won, {user_wins} times' )
print(f'The computer won, {computer_wins} times')

#final if else statement
if user_wins > computer_wins:
    print('Congrats!!! you are the winner')
else:
    print('You lost, good luck next time')   



#if player_hand != 'rock' or 'paper' or 'scissors':
    # print('Please enter a valid word next time')
     #quit()


    



