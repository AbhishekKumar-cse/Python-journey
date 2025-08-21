secretNumber = 9
guessCount = 0
guessLimit = 3

while guessCount < guessLimit:
    Number = int(input("Enter a number: "))
    
    if Number == secretNumber:
        print("You win!")
        break
    elif Number < secretNumber:
        print("Too low!")
    else:
        print("Too high!")
    
    guessCount += 1  # <-- increment outside of if-elif-else

if guessCount == guessLimit:
    print("You lose!")
