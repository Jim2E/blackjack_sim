import random
import numpy as np

bal = 100
quit_bal = 10
ten_card = ['10','J','Q','K']

def newdeck():
    deck = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    #six decks w/ 312 cards
    ndeck = deck*4*6
    return ndeck 

def start_deal(x):
    for j in range(2):
        if not td or len(td)==0:
            td = newdeck()
        draw = random.sample(td,1)[0]
        x.append(draw)
        td.remove(draw)

def blkjk(i):
    if 'A' in i and any(x in i for x in ten_card) and len(i)==2: return True
    else: return False

def basic_strategy(player,dealer):
    double_card = False
    dealer_upcard = dealer[0]
    
    if 'A' not in p_hand and len(set(player))!=1:
        p_hand = int(p_hand[0])+int(p_hand[1])
    elif 'A' in p_hand and len(set(player))==2:
        p_hand = 2


while(bal > quit_bal):
    bet = .05*bal
    #draw 2 player's and dealer's cards
    p = []
    d = []
    start_deal(p)
    start_deal(d)

    #check for blackjacks
    if blkjk(p) and blkjk(d):
        continue #push 
    elif blkjk(p):
        bal += (3/2)*bet
        continue
    elif blkjk(d):
        bal -= bet
        continue

    #implement basic strategy
    decision = basic_strategy(p,d)






