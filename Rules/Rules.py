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
        if points > 21:
            return True
        else:
            return False