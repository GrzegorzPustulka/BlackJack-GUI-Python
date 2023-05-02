from Cards.Deck import Deck


class Player(Deck):
    def __init__(self):
        super().__init__()
        self.current_money = 1000
        self.money_in_bet = 0
        self.money_to_win = 0
        self.points = 0
        self.points_split = 0
        self.hand_deck = []
        self.second_deck = []
        self.ace = 0
        self.ace_split = 0

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

    def set_points_split(self, points):
        self.points_split = points

    def get_points_split(self):
        return self.points_split

    def set_counter_ace(self, ace):
        self.ace = ace

    def get_counter_ace(self):
        return self.ace

    def set_counter_ace_split(self, ace_split):
        self.ace_split = ace_split

    def get_counter_ace_split(self):
        return self.ace_split

    def add_card(self, count, deck):
        for i in range(count):
            self.hand_deck.append(deck.primaryDeck[0])
            deck.remove_card_from_deck()

    def add_card_split(self, deck):
        self.second_deck.append(deck.primaryDeck[0])
        deck.remove_card_from_deck()

    def add_points(self):
        self.set_points(0)
        for i in range(len(self.hand_deck)):
            self.set_points(self.get_points() + self.deckPoint[self.hand_deck[i]])
            if 'Ace' in self.hand_deck[i]:
                self.set_counter_ace(self.get_counter_ace() + 1)

        while self.get_points() > 21 and self.get_counter_ace() > 0:
            self.set_points(self.get_points() - 10)
            self.set_counter_ace(self.get_counter_ace() - 1)

    def add_points_split(self):
        self.set_points_split(0)
        for i in range(len(self.second_deck)):
            self.set_points_split(self.get_points_split() + self.deckPoint[self.second_deck[i]])
            if 'Ace' in self.second_deck[i]:
                self.set_counter_ace_split(self.get_counter_ace_split() + 1)

        while self.get_points_split() > 21 and self.get_counter_ace_split() > 0:
            self.set_points_split(self.get_points_split() - 10)
            self.set_counter_ace_split(self.get_counter_ace_split() - 1)

    def check_burn(self):
        return self.get_points() > 21

    def clear_hand(self):
        self.hand_deck.clear()
        self.second_deck.clear()

    def split_cards(self):
        self.second_deck.append(self.hand_deck.pop())

    def check_split(self):
        first_card_end_index = self.hand_deck[0].find('-')
        second_card_end_index = self.hand_deck[1].find('-')
        return self.hand_deck[0][0:first_card_end_index] == self.hand_deck[1][0:second_card_end_index]
