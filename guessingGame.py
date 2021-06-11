import random
noOfGuesses=0
number = random.randrange(1,99)
print("Guessing Game")
print("Guess The from 1-100 in 8 guesses")
state=0


while(noOfGuesses<8 and state == 0):

    Guess=int(input("Type Your Guess : "))
    noOfGuesses=noOfGuesses+1

    if(number>Guess ):
        print("The Number Is Greater Than ",Guess)

    if(number<Guess ):
        print("The Number Is Smaller Than ",Guess)

    if(number==Guess ):
        print(" Yay You Won The Number Was",number)
        print("You Guessed It In ",noOfGuesses,"Guesses")
        state = 1

        
if(noOfGuesses>7 and state==1):
    print("You Ran Out Of Guesses The Number Was",number)


