import random
import numpy as np
from sympy import false


def newdeck():
    deck = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    #six decks w/ len 312
    ndeck = deck*4*6
    return ndeck 

def start_deal(x):
    for j in range(2):
        if len(td) == 0:
            td = newdeck()
        draw = random.sample(td,1)[0]
        x.append(draw)
        td.remove(draw)

def basic_strategy(player,dealer):
    double_flag = False
    d_upcard = dealer[0]
    if 'A' not in p_hand and len(set(player))!=1:
        p_hand = int(p_hand[0])+int(p_hand[1])
    elif 'A' in p_hand and len(set(player))==2:
        p_hand = 



money = 100

while(money != 0):
    #draw player's and dealer's cards
    p = []
    d = []
    start_deal(p)
    start_deal(d) 
        
    #implement basic strategy
    decision = basic_strategy(p,d)







a= [20,120]
s = random.sample(a, 1)
s.remove(s)
print(a)