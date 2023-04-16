from Cards.Deck import Deck


class Dealer(Deck):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.deck = []

    def set_points(self, points):
        self.points = points

    def get_points(self):
        return self.points

    def add_card(self, count, deck):
        for i in range(count):
            self.deck.append(deck.primaryDeck[0])
            deck.remove_card_from_deck()
            self.set_points(self.get_points() + deck.deckPoint[self.deck[0]])
