import random

def play(x):
    print("'r' for rock , 'p' for paper, 's' for scissor ")
    user = input("enter your choice")
    pc = random.choice(['r','p','s'])

    if user == pc :
        return 'Draw'
    
    # r>s , s>p , p>r
    if whos_the_winner(user,pc):
        return 'you won'
    
    return 'you lost '



def whos_the_winner(player , opponent ):
    # returning true if player wins
    # r>s , s>p , p>r
    
    if (player =='r' and opponent == 's')or(player == 's' and opponent == 'p')\
       or(player == 'p' and opponent == 'r'):
        return True 
    
x=int(input("enter hoe many time you need to paly : "))
while x != 0 :
    print(play(x))
    x=x-1 
    
              
                
                
                
                
            
    
