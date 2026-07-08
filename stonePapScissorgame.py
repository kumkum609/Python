print("This is Stone,Paper and Scissor game")
print("Get ready!")
print("Rule of this game :\nStone->st\nPaper->p \nScissor->sc")
import random
tie =0
c = 0
y =0
run =0
list =["st","p","sc"]
while(run<5):
    comp = random.choice(list)
    print("\nEnter your choice:")
    you =input()
    print("Computer choice=",comp)
    if (comp==you):
        print("Oh it's Tie")
        tie+=1
        run+=1
    elif(comp=='st' and you=='p'):
        print("You won")
        y+=1
        run+=1
    elif(comp=='p' and you=='sc'):
        print("You won")
        y+=1
        run+=1
    elif(comp=='sc' and you=='st'):
        print("You won")
        y+=1
        run+=1     
    elif(comp=='p' and you=='st'):
        print("Computer won")
        c+=1
        run+=1     
    elif(comp=='sc' and you=='p'):
        print("Computer won")
        c+=1
        run+=1
    elif(comp=='st' and you=='sc'):
        print("Computer won")
        c+=1
        run+=1
    else:
        print("Invalid choice")
    
if run ==5:
    print("\n===================")
    print("Game over")    
    print(f"Final score-> You:{y}| Computer:{c}|Tie:{tie}")
    if(c>y):    
        print("Computer wins the final match")
    elif(y>c):
        print("Congrats! You win the final match")
    else:
        print("It's a tie!")                             