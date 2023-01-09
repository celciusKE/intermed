playerA= input("Player A, whats your name: ")
playerB= input("Player B, whats  your name: ")


user1_answer= input("%s, do yo want to choose rock, paper or scissors?" % playerA)
user2_answer = input("%s, do you want to choose rock, paper or scissors?" % playerB)

def compare(u1,u2):
    if u1 == u2:
        print("Draw,We have to start over")
    elif u1 == 'rock':
        u2=='scissors'
        print('rock beats scissors')

    elif u1 == 'rock':
        u2 =='paper'
        print('Paper beats Rock')

    elif u1== 'paper':
        u2 =='scissors'
        print('Scissors beats paper')
    
    else:
        print('invalid input')
    
print(compare(user1_answer, user2_answer))
