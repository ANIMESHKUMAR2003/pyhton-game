#Code for stone paper scissors game in python



import random
def game(comp, you):
    
    if comp == you:
        return None

    
    elif comp == 's':
        if you=='p':
            return True
        elif you=='sc':
            return False
    
    
    elif comp == 'p':
        if you=='sc':
            return True
        elif you=='s':
            return False
    
    
    elif comp == 'sc':
        if you=='s':
            return True
        elif you=='p':
            return False;

print("Comp Turn: Stone(s) paper(p) or scissors(sc)?")
randNo = random.randint(1, 3) 
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 'sc'

you = input("Your Turn: Stone(s) Paper(p) or Scissors(sc)?")
a = game(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")
