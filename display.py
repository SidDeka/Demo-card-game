#display module

import pygame, random
from image_list_func import*
from placingcards import*


#initializing modules
pygame.init()

#Window size and background image
WIDTH = 800
HEIGHT = 600

#Making a display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background_img = pygame.image.load('wooden.png').convert()

#displaying cover card
cover = pygame.image.load('card_cover.png').convert_alpha()
cover1 = pygame.image.load('card_cover.png').convert_alpha()

#print(type(cover))



##------------------------------------------------------------------------------
##  Display functions
##------------------------------------------------------------------------------

#def display background
def draw_background():
    '''
    displays background by using an image that is loaded into the same file
    as the python file
    '''
    global screen
    global background_img
    global cover_loading
    global cover1_loading

    #screen.fill(pygame.color.Color('green'))
    background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT)) 
    screen.blit(background_img, (0, 0))


def draw_cover():
    '''
    displays card cover at the location of both players' decks
    '''
    global screen
    global cover
    global cover1


    cover = pygame.transform.scale(cover, (100,150))
    cover1 = pygame.transform.scale(cover1, (100,150))
    screen.blit(cover, (600, 410))
    screen.blit(cover1, (100, 410))

    return cover, cover1
   

def draw_card_1():
    '''
    takes input of most recent or newest card on the deck and draws it
    '''
    global played_deck

    center_image_1 = played_deck[0]+".png"

    center_deck_image_1 = pygame.image.load(center_image_1).convert_alpha()
    center_deck_image_1 = pygame.transform.scale(center_deck_image_1 , (100,160))
    screen.blit(center_deck_image_1, (310,100))
    

    return center_deck_image_1

def draw_card_2():
    
    global played_deck
  
    center_image_2 = played_deck[1]+".png"
        
   
    
    center_deck_image_2 = pygame.image.load(center_image_2).convert_alpha()
    center_deck_image_2 = pygame.transform.scale(center_deck_image_2 , (100,160))
    screen.blit(center_deck_image_2, (350,100))

    return center_deck_image_2


def draw_card_3():

    global played_deck

    center_image_3 = played_deck[2]+".png"
    
    center_deck_image_3 = pygame.image.load(center_image_3).convert_alpha()
    center_deck_image_3 = pygame.transform.scale(center_deck_image_3 , (100,160))
    screen.blit(center_deck_image_3, (380,100))

    return center_deck_image_3
'''
def onscreen_text():
    global player1_cardcount 
    global player2_cardcount
    global centerdeck_cardcount


    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    strp1deck = str(player1_cardcount)
    p1pointtext = myfont.render(f'Player 1: {strp1deck}', 1, 'red')
    screen.blit(p1pointtext, (0,0))#(10,750))
    #screen.blit(p1pointst,(10,750))


    
    myfont2 = pygame.font.SysFont('Comic Sans MS', 30)
    strp2deck = str(player2_cardcount)
    p2pointtext = myfont2.render(f'Player 2: {strp2deck}', 1, 'white')
    screen.blit(p2pointtext, (WIDTH - 225, 0))

    myfont3 = pygame.font.SysFont('Comic Sans MS', 30)
    strcdeck = str(centerdeck_cardcount)
    cpointtext = myfont2.render(f'Center Deck: {strcdeck}', 1, 'white')
    screen.blit(cpointtext, (WIDTH - 450, 0))
 
    return p1pointtext, p2pointtext, cpointtext

'''    
