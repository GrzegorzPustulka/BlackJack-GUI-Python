import random


class Deck:
    def __init__(self):
        self.how_many_decks = 8

        self.primaryDeck = ["Two-Spades", "Two-Hearts", "Two-Clubs", "Two-Diamonds",
                            "Three-Spades", "Three-Hearts", "Three-Clubs", "Three-Diamonds",
                            "Four-Spades", "Four-Hearts", "Four-Clubs", "Four-Diamonds",
                            "Five-Spades", "Five-Hearts", "Five-Clubs", "Five-Diamonds",
                            "Six-Spades", "Six-Hearts", "Six-Clubs", "Six-Diamonds",
                            "Seven-Spades", "Seven-Hearts", "Seven-Clubs", "Seven-Diamonds",
                            "Eight-Spades", "Eight-Hearts", "Eight-Clubs", "Eight-Diamonds",
                            "Nine-Spades", "Nine-Hearts", "Nine-Clubs", "Nine-Diamonds",
                            "Ten-Spades", "Ten-Hearts", "Ten-Clubs", "Ten-Diamonds",
                            "Jack-Spades", "Jack-Hearts", "Jack-Clubs", "Jack-Diamonds",
                            "Queen-Spades", "Queen-Hearts", "Queen-Clubs", "Queen-Diamonds",
                            "King-Spades", "King-Hearts", "King-Clubs", "King-Diamonds",
                            "Ace-Spades", "Ace-Hearts", "Ace-Clubs", "Ace-Diamonds",
                            ] * self.how_many_decks

        self.deckPoint = {
            "Two-Spades": 2, "Two-Hearts": 2, "Two-Clubs": 2, "Two-Diamonds": 2,
            "Three-Spades": 3, "Three-Hearts": 3, "Three-Clubs": 3, "Three-Diamonds": 3,
            "Four-Spades": 4, "Four-Hearts": 4, "Four-Clubs": 4, "Four-Diamonds": 4,
            "Five-Spades": 5, "Five-Hearts": 5, "Five-Clubs": 5, "Five-Diamonds": 5,
            "Six-Spades": 6, "Six-Hearts": 6, "Six-Clubs": 6, "Six-Diamonds": 6,
            "Seven-Spades": 7, "Seven-Hearts": 7, "Seven-Clubs": 7, "Seven-Diamonds": 7,
            "Eight-Spades": 8, "Eight-Hearts": 8, "Eight-Clubs": 8, "Eight-Diamonds": 8,
            "Nine-Spades": 9, "Nine-Hearts": 9, "Nine-Clubs": 9, "Nine-Diamonds": 9,
            "Ten-Spades": 10, "Ten-Hearts": 10, "Ten-Clubs": 10, "Ten-Diamonds": 10,
            "Jack-Spades": 10, "Jack-Hearts": 10, "Jack-Clubs": 10, "Jack-Diamonds": 10,
            "Queen-Spades": 10, "Queen-Hearts": 10, "Queen-Clubs": 10, "Queen-Diamonds": 10,
            "King-Spades": 10, "King-Hearts": 10, "King-Clubs": 10, "King-Diamonds": 10,
            "Ace-Spades": 11, "Ace-Hearts": 11, "Ace-Clubs": 11, "Ace-Diamonds": 11}

        random.shuffle(self.primaryDeck)

        self.cards_image = {}

        for key in self.deckPoint.keys():
            self.cards_image[key] = "images/cards/" + key + ".png"

    def remove_card_from_deck(self):
        self.primaryDeck.pop(0)
