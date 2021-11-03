# Sheena Wolliston

import random
import CardAbbr


def make_deck():
    """
    Makes deck of cards from file card.py.
    Adds rank and suit together in order to make 52 unique cards.
    :return:
    """
    deck = []
    for suit in CardAbbr.LIST_OF_SUITS:
        for rank in CardAbbr.LIST_OF_RANKS:
            new_card = CardAbbr.make_card(suit, rank)
            deck.append(new_card)
    return shuffle(deck)


def shuffle(cards):
    """
    Shuffles the deck of 52 cards.
    :param cards:
    :return: the shuffled deck
    """
    random.shuffle(cards)
    return cards



def draw_card(cards):
    """
    Draws 1st card from deck and returns that card to the user
    :param cards:
    :return:
    """
    top_card = cards[0]
    cards.remove(top_card)
    return top_card


def is_deck_empty(cards):
    """
    If a card is trying to be drawn from an empty deck False will be return
    If a card is trying to be drawn from a deck that has cards return true
    :param cards:
    :return:
    """
    if cards != []:
        return False
    else:
        return True


def __test_deck():
    testing_deck = make_deck()
    print(testing_deck)
    shuffle(testing_deck)
    print(testing_deck)
    print(len(testing_deck))
    print(draw_card(testing_deck))
    print(testing_deck)
    print(len(testing_deck))


if __name__ == "__main__":
    __test_deck()
