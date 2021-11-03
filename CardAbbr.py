#Sheena Wolliston


LIST_OF_RANKS = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
LIST_OF_SUITS = ["H","S","D","C"]

def make_card(rank, suit):
    """
    Makes a card with rank before the suit.
    Then returns card
    :param rank:
    :param suit:
    :return:
    """
    card = rank + suit
    return card


def get_rank(card):
    """
    Returns the rank of the card
    :param card:
    :return:
    """
    rank = card[0]
    return rank

def get_suit(card):
    """
    Returns suit of the card
    :param card:
    :return:
    """
    suit = card[1:len(card)]
    return suit

'''
def __test_card():
    testing_card = make_card("4", "S")
    print(testing_card)
    print(get_suit(testing_card))
    print(get_rank(testing_card))

if __name__ == "__main__":
    __test_card()
'''
