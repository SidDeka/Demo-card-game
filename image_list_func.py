#list of suits and ranks]
import Deck_of_Cards

def images_list():
    global LIST_OF_RANKS
    global LIST_OF_SUITS

    images = []
    image_files = []
    for s in  LIST_OF_RANKS:
        for r in LIST_OF_SUITS:
            #image = pygame.image.load(f"{s}{r}.png").convert_alpha()
            #image = pygame.transform.scale(image , (100,160))
            image = f"{s}{r}.png"
            images.append(image)
        return images
