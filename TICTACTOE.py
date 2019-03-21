import os
import time
from TICTACTOE_FUNCTIONS import tictactoe_openinggame,returnpick,tictactoe_draw,tictactoe_endgame

def tictactoe_game():
    from random import randint
    stop=False
    a=b=c=d=e=f=g=h=i=' '
    x = tictactoe_openinggame()
    player1 = x[0]
    player2 = x[1]
    print('Welcome to the TIC TAC TOE game!')
    counting = 0
    while stop==False:
        if counting%2==0:
            pick=player1
            print('Player 1 turn')
        elif counting%2!=0:
            pick=player2
            print('Player 2 turn')
        location = input('Enter location: ')
        os.system('cls')
        x = returnpick(location,pick,a,b,c,d,e,f,g,h,i)
        [a,b,c,d,e,f,g,h,i] = [x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]]
        tictactoe_draw(a,b,c,d,e,f,g,h,i)
        stop = tictactoe_endgame(a,b,c,d,e,f,g,h,i,player1,player2)
        counting+=1
tictactoe_game()