class Rules:
    def __init__(self):
        pass

    def check_BlackJack(self, player):
        seven = 0
        if player.get_points() == 21 and len(player.hand_deck) == 2:
            return True
        elif player.get_points() == 21 and len(player.hand_deck) == 3:
            for card in player.hand_deck:
                if 'Seven' in card:
                    seven += 1
                else:
                    return False
            if seven == 3:
                return True
        return False

    def checkBurn(self, points):
        return points > 21

    def check_win(self, player_points, dealer_points):
        return player_points > dealer_points

    def check_draw(self, player_points, dealer_points):
        return player_points == dealer_points

    def check_BlackJack_split(self, player):
        seven = 0
        if player.get_points_split() == 21 and len(player.second_deck) == 2:
            return True
        elif player.get_points_split() == 21 and len(player.second_deck) == 3:
            for card in player.second_deck:
                if 'Seven' in card:
                    seven += 1
                else:
                    return False
            if seven == 3:
                return True
        return False
