import random

    
def condition(a,b,actual):
    guess = int(input(f"Guess a number b/w {a} and {b}: "))
    c=1
    while guess!= actual:
        if guess<actual:
            c+=1
            guess = int(input(f"Too loww.\nGuess a number b/w {a} and {b}: "))
        else :
            c+=1
            guess = int(input(f"Too high.\nGuess a number b/w {a} and {b}: "))
    print(f"You guessed the correct number in {c} guesses.")
    return c




if __name__=="__main__":
    a= int(input("Enter a number: "))
    b= int(input("Enter another number: "))
    random_number1 = random.randint(a,b)
    random_number2 = random.randint(a,b)

    print("\nPlayer 1's TURN\n")
    g1=condition(a,b,random_number1)
    print("\nPlayer 2's TURN\n")
    g2=condition(a,b,random_number2)

    if g1 < g2:
        print("\nPLAYER 1 WON!!!\n")

    elif g1>g2:
        print("\nPLAYER 2 WON!!\n")
    else:
        print("\nITS A TIE\n")
    print(f"The number for player 1 was {random_number1}\nThe number for player 2 was {random_number2}")


        
