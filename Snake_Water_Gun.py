import random

r = random.randint(1,3)


print('Enter Snake(s), Water(W), Gun(G)')

if r == 1:
    comp = 'S'
elif r == 2:
    comp = 'W'
else:
    comp = 'G'    
    

you = input('Enter Snake(s), Water(W), Gun(G)\n')

print(f'Computer Choose {comp}')
print(f'You Choose {you}')

def Game(comp, you):
    if comp == you:
        print('Game tie')
    if comp == 'S' and you == 'W':
        return False
    elif comp == 'W' and you == 'G':
        return False
    elif comp == 'G' and you == 'S':
        return False
    

    if comp == 'S' and you == 'G':
        return True
    elif comp == 'W' and you == 'S':
        return True
    elif comp == 'G' and you == 'W':
        return True
    


a = Game(comp, you)

if a == False:
    print("You Loss")
              
elif a == True:
    print("You Win")

     
      
        

