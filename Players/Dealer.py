from Deck.Deck import Deck


class Dealer(Deck):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.hand_deck = []
        self.ace = 0

    def set_counter_ace(self, ace):
        self.ace = ace

    def get_counter_ace(self):
        return self.ace

    def set_points(self, points):
        self.points = points

    def get_points(self):
        return self.points

    def clear_hand(self):
        self.hand_deck.clear()

    def add_card(self, deck):
        self.hand_deck.append(deck.primaryDeck[0])
        deck.remove_card_from_deck()
        self.add_points()

    def add_card_over_16(self, deck):
        while self.get_points() <= 16:
            self.hand_deck.append(deck.primaryDeck[0])
            deck.remove_card_from_deck()
            self.add_points()

    def add_points(self):
        self.set_points(0)
        for i in range(len(self.hand_deck)):
            self.set_points(self.get_points() + self.deckPoint[self.hand_deck[i]])
            if 'Ace' in self.hand_deck[i]:
                self.set_counter_ace(self.get_counter_ace() + 1)

        while self.get_points() > 21 and self.get_counter_ace() > 0:
            self.set_points(self.get_points() - 10)
            self.set_counter_ace(self.get_counter_ace() - 1)

        self.set_counter_ace(0)
