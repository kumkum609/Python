#Guess the number game
n=18
i=0
print("Guess the number game")
while(i<5):
    print("number of guesses= ",i+1)
    print("Enter the number:")
    x =int(input())
    if x<18:
        print("You guessed smaller number")
    elif x>18:
        print("You guessed Larger number")
    else:
        print("Congrats! You win")

        print("You guessed correct number")     
        break
    i+=1
if i==5:
    print("Game over")  
    print("Try again")  
    

       