import random
ASK=input(('DO YOU WANNA MAKE THE COMPUTER GUESS(C) OR YOU WANNA GUESS(I) ?')).lower()

def guess(x):
    random_number= random.randint(1,x)
    guess=0
    while guess !=random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess< random_number:
            print("Nice try,but its too loww you peasant.")
        elif guess > random_number :
            print ("Pfft! Too high you dumbass")

    print(f'Hah, you guessed it right,its {random_number}.Never expected you to win tho')

def guess2(x):
    print('Think of a number for the computer to guess ')
    low=1
    high=x
    feedback=''
    while feedback!='c':
        try:
            if low!=high:
                guess = random.randint(low,high)
            else :
                guess=low #doesnt matter coz low=high
            feedback= (input(f'Is     {guess}  too high(H),   too low(L) or   correct(C)?  ')).lower()
            if feedback == 'h' :
                high= guess-1
            elif feedback =='l':
                low = guess+1
        except:
            print('You do realise that you are not making any sense right?')
            quit()
    print('LOL congrats ma mahn ! The computer understood your stupid number.')



if ASK== 'i':
    guess(10)
elif ASK== 'c':   
    guess2(10)
else:
    print ('IF YOU DIDNT WANTED TO PLAY WHY THE HECK DID YOU COME!!')
    quit()