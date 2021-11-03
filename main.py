#main.py

import pygame, random
from display import*
from image_list_func import *
from Deck_of_Cards import *
from placingcards import*
from prev_deck_list import*
from CardAbbr import*
from game_rules import*


#initializing modules
pygame.init()
clock = pygame.time.Clock()
#test variables
running = True
player1_cardcount = len(deck1)
player2_cardcount = len(deck2)
centerdeck_cardcount = len(played_deck)



##------------------------------------------------------------------------------
##  Game loop
##------------------------------------------------------------------------------
def p1_wins():
    
    myfont = pygame.font.SysFont('Comic Sans MS', 25)
    p1_win_text = myfont.render('Player 1 wins', 1, 'white')
    screen.blit(p1_win_text, (300,280))

    return p1_win_text

def p2_wins():
    
    myfont = pygame.font.SysFont('Comic Sans MS', 25)
    p2_win_text = myfont.render('Player 2 wins', 1, 'white')
    screen.blit(p2_win_text, (300,280))

    return p2_win_text

def onscreen_text():
    global player1_cardcount 
    global player2_cardcount
    global centerdeck_cardcount


    myfont = pygame.font.SysFont('Comic Sans MS', 20)
    strp1deck = str(player1_cardcount)
    p1pointtext = myfont.render(f'Player 1: {strp1deck}', 1, 'red')
    screen.blit(p1pointtext, (0,0))#(10,750))
    #screen.blit(p1pointst,(10,750))


    
    myfont2 = pygame.font.SysFont('Comic Sans MS', 20)
    strp2deck = str(player2_cardcount)
    p2pointtext = myfont2.render(f'Player 2: {strp2deck}', 1, 'white')
    screen.blit(p2pointtext, (WIDTH - 225, 0))

 
    return p1pointtext, p2pointtext

def q_text():
    myfont = pygame.font.SysFont('Comic Sans MS', 20)
    q_text = myfont.render('Player 1 press Q to drops cards', 1, 'red')
    screen.blit(q_text, (0, 45))

    return q_text

def p_text():
    myfont = pygame.font.SysFont('Comic Sans MS', 20)
    p_text = myfont.render('Player 2 press P to drop cards', 1, 'white')
    screen.blit(p_text, (WIDTH - 300, 45))

    return p_text


def l_text():
    myfont = pygame.font.SysFont('Comic Sans MS', 20)
    l_text = myfont.render('Player 1 press L to slap', 1, 'red')
    screen.blit(l_text, (0, 90))

    return l_text

def a_text():
    myfont = pygame.font.SysFont('Comic Sans MS', 20)
    a_text = myfont.render('Player 2 press A to slap', 1, 'white')
    screen.blit(a_text, (WIDTH - 300, 90))

    return a_text

game_rules()
while running == True:
    clock.tick(60)
    
    count1 = 0
    count2 = 0
    facecard_played = False

   

    
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
            

       
        elif event.type == pygame.KEYDOWN:
            
            # Key pressed event
            press_button = event.dict['key']
            print()
            print("Key pressed = %s" % press_button)

            if press_button == ord('q') and player_turn:
                if len(played_deck) != 0:
                    played_deck.insert(0, deck1[0])
                    centerdeck_cardcount += 1
                    deck1.pop(0)
                    player1_cardcount -= 1
                    player_turn = False
                    print(played_deck)
                    if 'A' in played_deck[0]:
                        facecard_played = True
                else:
                    played_deck.append(deck1[0])
                    centerdeck_cardcount += 1
                    deck1.pop(0)
                    player1_cardcount -= 1
                    player_turn = False
                    print(played_deck)
                 

            elif press_button == ord('p') and not(player_turn):
                if len(played_deck) != 0:
                    played_deck.insert(0, deck2[0])
                    centerdeck_cardcount += 1
                    deck2.pop(0)
                    player2_cardcount -= 1
                    player_turn = True
                    print(played_deck)
                    if 'A' in played_deck[0]:
                        facecard_played = True
                else:
                    played_deck.append(deck2[0])
                    centerdeck_cardcount += 1
                    deck2.pop(0)
                    player2_cardcount -= 1
                    player_turn = True
                    print(played_deck)

            elif press_button == ord('l'):
                slap_time()
                if slap_time() == True:
                    deck1.extend(played_deck)
                    print(deck1)
                    player1_cardcount = len(deck1)
                    played_deck.clear()
                    centerdeck_cardcount = 0
                    print(played_deck)
                else:
                    print('Not slap time')

            elif press_button == ord('a'):
                slap_time()
                if slap_time() == True:
                    deck2.extend(played_deck)
                    print(deck2)
                    player2_cardcount = len(deck2)
                    played_deck.clear()
                    centerdeck_cardcount = 0
                    print(played_deck)
                else:
                    print('Not slap time')
           



##------------------------------------------------------------------------------
##  Update display
##------------------------------------------------------------------------------

    if len(played_deck) > 2:
        draw_background()
        if len(deck1) == 0:
            draw_background()
            p2_wins()
            clock.tick(0)
        elif len(deck2) == 0:
            draw_background()
            p1_wins()
            clock.tick(0)

        draw_card_3()

    if len(played_deck) > 1:
        if len(played_deck) > 2:
            print()
        else:
            draw_background()

        draw_card_2()
        
    if len(played_deck) > 0:
        if len(played_deck) > 1:
            print()
        else:
            draw_background()
            
        slap_time()
        draw_cover()
        onscreen_text()
        q_text()
        p_text()
        a_text()
        l_text()
        draw_card_1()
        pygame.display.update()


    if len(played_deck) == 0:
        draw_background()
        draw_cover()
        onscreen_text()
        q_text()
        p_text()
        a_text()
        l_text()
        pygame.display.update()  

   
        
    
 
   
        
  
    
pygame.quit()
    
