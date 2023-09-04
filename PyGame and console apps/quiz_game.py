print("Wellcome to this quiz")
print('Note: make sure you type all your answers in lowercase exept names')
score = 0
playing = input('Do you want to play? ')

if playing.lower() != 'yes':
    quit()

print("Let's play then")


def question(q, a):
    q = input(q).lower()
    if q == a:
        print('Correct')
        score += 1
    else:
        print("Incorrect")
        score -= 1

question('Have you been to Mars?', 'no')
question('What does RAM stand for?', 'random access memory')
question('What does CPU stand for?','central processing unit')

yes

   
end = input('Do you want to see your final score?')

if end == 'yes':
     print(str(score))
else:
    print('Bye!!!')