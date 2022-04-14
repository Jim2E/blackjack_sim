import random
import numpy as np

bal = 100
quit_bal = 10
ten_card = ['10','J','Q','K']
val = {'A':11,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}
val2 = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}

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

def deal(x):
    if not td or len(td)==0:
            td = newdeck()
    draw = random.sample(td,1)[0]
    np.insert(x,-1,draw)
    td.remove(draw)


def blkjk(i):
    if 'A' in i and any(x in i for x in ten_card) and len(i)==2: return True
    else: return False

def cval(x):
    return val[x]

def basic_strategy(player,dealer):
    double_card = False
    phv = 0
    plyr = np.array(player)
    plyr_ace_count = np.where(plyr=='A')[0][1]

    dealer_upcard = dealer[0]
    dhv = 0
    dlr = np.array(dealer)
    dlr_ace_count = np.where(dlr=='A')[0][1]

    for i in range(len(player)):
        phv += val[player[i]]

    if len(plyr)==2 and len(set(plyr))==1:
        double_card=True

    if phv > 21 and plyr_ace_count >=1:
        nphv = phv - 10*plyr_ace_count
        nphv2 = phv - 10*(plyr_ace_count-1) 
        if nphv > 21 and nphv2 > 21:
            return 'bust'
        elif nphv<=21 and nphv > dhv:
            return 'win'
        elif nphv2<=21 and nphv2 > dhv:
            return 'win'
        elif nphv==dhv or nphv2==dhv:

    elif phv in [5,6,7,8] and not double_card:
        deal(plyr)
        basic_strategy(plyr,dlr)
    elif phv==9 and dealer_upcard in ['2','7','8','9','10','J','Q','K']:

    
    if 'A' not in player and len(set(player))!=1:
        


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
    outcome = basic_strategy(p,d)

    if outcome=='win':
        bal += bet
        continue
    elif outcome=='push':
        continue
    else:
        bal -=bet
    






