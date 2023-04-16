from Cards.Deck import Deck


class Player(Deck):
    def __init__(self):
        super().__init__()
        self.current_money = 1000
        self.money_in_bet = 0
        self.money_to_win = 0
        self.points = 0
        self.hand_deck = []

    def set_current_money(self, current_money):
        self.current_money = current_money

    def get_current_money(self):
        return self.current_money

    def set_money_in_bet(self, money_in_bet):
        self.money_in_bet = money_in_bet

    def get_money_in_bet(self):
        return self.money_in_bet

    def set_money_to_win(self, money_to_win):
        self.money_to_win = money_to_win

    def get_money_to_win(self):
        return self.money_to_win

    def set_points(self, points):
        self.points = points

    def get_points(self):
        return self.points

    def add_card(self, count, deck):
        for i in range(count):
            self.hand_deck.append(deck.primaryDeck[0])
            deck.remove_card_from_deck()

    def add_points(self):
        self.set_points(0)
        for i in range(len(self.hand_deck)):
            self.set_points(self.get_points() + self.deckPoint[self.hand_deck[i]])

    def check_burn(self):
        if self.get_points() > 21:
            return True
        else:
            return False

    def clear_hand(self):
        self.hand_deck.clear()
