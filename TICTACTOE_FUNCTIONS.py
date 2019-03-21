import os
import time

def returnpick(location,pick,a,b,c,d,e,f,g,h,i):
    if location == 'a' or location == 'A':
        a = pick
    elif location == 'b' or location == 'B':
        b = pick
    elif location == 'c' or location == 'C':
        c = pick
    elif location == 'd' or location == 'D':
        d = pick
    elif location == 'e' or location == 'E':
        e = pick
    elif location == 'f' or location == 'F':
        f = pick
    elif location == 'g' or location == 'G':
        g = pick
    elif location == 'h' or location == 'H':
        h = pick
    elif location == 'i' or location == 'I':
        i = pick
    return a,b,c,d,e,f,g,h,i

def tictactoe_draw(a,b,c,d,e,f,g,h,i):
    draw = []
    for y in range(1, 14):
        if y == 1 or y == 5 or y == 9 or y == 13:
            for x in range(0, 90):
                if x < 30:
                    draw.append('#')
                elif x >= 30 and x < 60:
                    draw.append(' ')
                elif x >= 60:
                    draw.append('#')
            print(''.join(draw))
            draw = []
        elif y == 3:
            for x in range(0, 90):
                if x == 0 or x == 9 or x == 19 or x == 29 or x == 60 or x == 69 or x == 79 or x == 89:
                    draw.append('#')
                elif x == 5:
                    if a == ' ':
                        draw.append('a')
                    else:
                        draw.append(' ')
                elif x == 14:
                    if b == ' ':
                        draw.append('b')
                    else:
                        draw.append(' ')
                elif x == 24:
                    if c == ' ':
                        draw.append('c')
                    else:
                        draw.append(' ')
                elif x == 65:
                    draw.append(a)
                elif x == 74:
                    draw.append(b)
                elif x == 84:
                    draw.append(c)
                else:
                    draw.append(' ')
            print(''.join(draw))
            draw = []
        elif y == 7:
            for x in range(0, 90):
                if x == 0 or x == 9 or x == 19 or x == 29 or x == 60 or x == 69 or x == 79 or x == 89:
                    draw.append('#')
                elif x == 5:
                    if d == ' ':
                        draw.append('d')
                    else:
                        draw.append(' ')
                elif x == 14:
                    if e == ' ':
                        draw.append('e')
                    else:
                        draw.append(' ')
                elif x == 24:
                    if f == ' ':
                        draw.append('f')
                    else:
                        draw.append(' ')
                elif x == 65:
                    draw.append(d)
                elif x == 74:
                    draw.append(e)
                elif x == 84:
                    draw.append(f)
                else:
                    draw.append(' ')
            print(''.join(draw))
            draw = []
        elif y == 11:
            for x in range(0, 90):
                if x == 0 or x == 9 or x == 19 or x == 29 or x == 60 or x == 69 or x == 79 or x == 89:
                    draw.append('#')
                elif x == 5:
                    if g == ' ':
                        draw.append('g')
                    else:
                        draw.append(' ')
                elif x == 14:
                    if h == ' ':
                        draw.append('h')
                    else:
                        draw.append(' ')
                elif x == 24:
                    if i == ' ':
                        draw.append('i')
                    else:
                        draw.append(' ')
                elif x == 65:
                    draw.append(g)
                elif x == 74:
                    draw.append(h)
                elif x == 84:
                    draw.append(i)
                else:
                    draw.append(' ')
            print(''.join(draw))
            draw = []
        else:
            for x in range(0, 90):
                if x == 0 or x == 9 or x == 19 or x == 29 or x == 60 or x == 69 or x == 79 or x == 89:
                    draw.append('#')
                else:
                    draw.append(' ')
            print(''.join(draw))
            draw = []

def tictactoe_endgame(a,b,c,d,e,f,g,h,i,player1,player2):
    if a!=' ' and b!=' ' and c!=' ' and d!=' ' and e!=' ' and f!=' ' and g!=' ' and h!=' ' and i!=' ':
        print('Game over')
        stop=True
    elif (a==b==c and a!=' ') or (a==d==g and a!=' ') or (a==e==i and a!=' '):
        if a==player1:
            print('player1 won!')
        else:
            print('player2 won!')
        stop=True
    elif d==e==f and d!=' ':
        if d==player1:
            print('player1 won!')
        else:
            print('player2 won!')
        stop=True
    elif g==h==i and g!=' ':
        if g==player1:
            print('player1 won!')
        else:
            print('player2 won!')
        stop=True
    elif b==e==h and b!=' ':
        if b==player1:
            print('player1 won!')
        else:
            print('player2 won!')
        stop=True
    elif (c==f==i and c!=' ') or (c==e==g and c!= ' '):
        if c==player1:
            print('player1 won!')
        else:
            print('player2 won!')
        stop=True
    else:
        stop=False

    return stop

def tictactoe_opponentlocation(a,b,c,d,e,f,g,h,i,player1,player2):
    alphabet = ['a','b','c','d','e','f','g','h','i']


def tictactoe_openinggame():
    from random import randint
    choice=['O','X']
    player1=choice[randint(0,1)]
    if player1=='X':
        player2='O'
        print('Player 1(X) and Player 2(O)')
    else:
        player2='X'
        print('Player 1(O) and Player 2(X)')
    return player1,player2