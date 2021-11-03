#Sydney Berger

#PLACING CARDS INTO CENTER DECK!!!!!!!! will be based off key press but is automatic right now 

import pygame
from Deck_of_Cards import *

shuffleddeck = make_deck()
deck1 = shuffleddeck[0:26]
deck2 = shuffleddeck[26:]
played_deck = []
player_turn = True #returns true while player 1 turn false when player 2 turn
p1_points = 0
p2_points = 0

pygame.init()



events = pygame.event.get()
for event in events:
    if event.type == pygame.QUIT:
        running = False  
        
    elif event.type == pygame.KEYDOWN:
        
        # Key pressed event
        press_button = event.dict['key']



def slap_time():
    '''
    checks if the players should slap by checking the first 2 indicies of
    the played_deck list
    if slap = false then the player pressing the button will not do anything

    '''
    global played_deck

    if len(played_deck) == 2:
        slap_check1 = played_deck[0][1]
        slap_check2 = played_deck[1][1]
        
    
        if len(played_deck) == 1:
            return False
        elif slap_check1 == slap_check2:
                return True #if it is matching
        
        elif 'K' in played_deck[0] and 'Q' in played_deck[1] or 'K' in played_deck[1] and 'Q' in played_deck[0]:
                return True
        else: #no slap
                return False

    if len(played_deck) >= 2:
        slap_check1 = played_deck[0][1]
        slap_check2 = played_deck[1][1]
        slap_check3 = played_deck[2][1]
    
        if len(played_deck) == 1:
            return False
        elif slap_check1 == slap_check2:
            return True #if it is matching
        elif slap_check1 == slap_check3:
            return True #check if it is a sandwhich
        
        elif 'K' in played_deck[0] and 'Q' in played_deck[1] or 'K' in played_deck[1] and 'Q' in played_deck[0]:
            return True
        elif played_deck[0][0] == played_deck[1][0]:
            return True
        elif ('S' in played_deck[0] or 'C' in played_deck[0]) and ('S' in played_deck[1] or 'C' in played_deck[1]) and ('S' in played_deck[2] or 'C' in played_deck[2]):
            return True
        elif ('H' in played_deck[0] or 'D' in played_deck[0]) and ('H' in played_deck[1] or 'D' in played_deck[1]) and ('H' in played_deck[2] or 'D' in played_deck[2]):
            return True
        else: #no slap
            return False
        
    else:
        return False


def p1points():
    '''
    Gives p1points - so points are tracked on the not main file 
    '''
    p1_points += 1
    print(p1_points)
    

def p2points():
    p2_points += 1
    print(p2_points)







