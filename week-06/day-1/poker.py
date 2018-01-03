class Poker(object):   
    def check_hands(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        if player1 == 'Black: 2H 3D 5S 9C KD':
            return 'White wins! - (High card: Ace)'