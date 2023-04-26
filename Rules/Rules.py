class Rules:
    def __init__(self):
        pass

    def check_BlackJack(self, player):
        blackJack = False
        if player.get_points() == 21 and len(player.hand_deck) == 2:
            blackJack = True
        elif player.get_points() == 21 and len(player.hand_deck) == 3:
            for card in player.hand_deck:
                if 'Seven' not in card:
                    break
            blackJack = True
        return blackJack

    def checkBurn(self, points):
        return points > 21

    def check_win(self, player_points, dealer_points):
        return player_points > dealer_points

    def check_draw(self, player_points, dealer_points):
        return player_points == dealer_points
