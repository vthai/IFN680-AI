
class Player(object):
    def play(self, move):
        pass

class HumanPlayer(Player):
    def __init__(self, gameboard):
        self.gameboard = gameboard

    def play(self, move):
        self.gameboard.record(move)
        while True:
            # move is an integer specifying the index of the cell played
            m = int(input("Your Move -> "))
            if m not in self.gameboard.legal_moves():
                print ("Error: illegal move")
                continue
            break
        self.gameboard.record(m)
        return m 