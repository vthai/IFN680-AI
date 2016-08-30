
from sets import Set

import array
import player

class TicTacToeBoard(object):

    def __init__(self, n):
        self.n = n
        self.board = array.array('b', [0]*n*n)
        self.symbol = {0: '.', 1: 'x', -1: 'o'}
        self.turn = 1;

    def display(self):
        print ''
        for r in range(self.n):
            print (' ' * 5),
            for c in range(self.n):
                print self.symbol[self.board[r * self.n + c]],
            print ''
        print ''

    def clone(self):
        t3 = TicTacToeBoard(self.n)
        #t3 = elf.board[:]
        return t3

    def i2rc(self,i):
        '''
        Convert from i index to row, column
        '''
        return  i/self.n, i%self.n


    def rc2i(self,r,c):
        '''
        Convert from row, column to i index 
        '''
        return r*self.n+c

    def record(self, move):
        #print 'recording', move, 'for player', self.turn
        if move is not None:
            self.board[move] = self.turn
            self.turn = self.turn * -1

    def legal_moves(self):
        return [i for i in range(self.n * self.n) if self.board[i] == 0]

    def game_ends(self, last_move):
        if last_move is None:
            return False
        # horizontal
        left = last_move - 3 if last_move - 3 >= 0 else 0
        right = last_move + 3 if last_move + 3 < self.n else self.n - 1
        print 'left, right', left, right
        sum = 0;
        for i in range(left, right + 1):
            sum = sum + self.board[i]

        print 'sum h', sum
        if sum != 3 and sum != -3:
            top = (last_move - self.n)%self.n if (last_move - self.n)%self.n >= 0 else last_move - self.i2rc(last_move)[0]*self.n
            down = (last_move + self.n * 2) if (last_move + self.n * 2) < self.n * self.n else last_move + (self.n * (self.n - self.i2rc(last_move)[0] - 1))
            sum = 0
            for i in range(top, down/self.n + 1):
                sum = sum + self.board[i * self.n]

        last_move_player = self.turn * -1
        if last_move_player == 1 and sum == 3:
            return True
        elif last_move_player == -1 and sum == -3:
            return True
        return False

class Game(object):

    def __init__(self, n=3):
        self.t3_board = TicTacToeBoard(n)
        self.player1 = player.HumanPlayer(self.t3_board.clone())
        self.player2 = player.HumanPlayer(self.t3_board.clone())
        self.players = {1: self.player1, -1: self.player2}

    def start(self):
        last_move = None

        while not self.t3_board.game_ends(last_move):
            self.t3_board.display()
            print 'Player %s to move ' %('Black' if self.t3_board.turn == -1 else 'White')
            move = self.players[self.t3_board.turn].play(last_move)
            self.t3_board.record(move)
            last_move = move

        print 'Game ends'
        self.t3_board.display()


if __name__ == '__main__':
    print 'Tic Tac Toe game'

    game = Game()
    game.start()
