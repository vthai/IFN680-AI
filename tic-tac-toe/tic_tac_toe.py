
from sets import Set

import array
import player

class TicTacToeBoard(object):

    def __init__(self, n):
        self.n = n
        self.board = array.array('b', [0]*n*n)
        self.symbol = {0: '.', 1: 'x', -1: 'o'}
        self.potential_win = {}
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
        print 'recording', move, 'for player', self.turn
        if move is not None:
            self.board[move] = self.turn

            append_list = []

            left = move - 1 if move%self.n > 0 else None
            right = move + 1 if move%self.n < self.n - 1 else None
            if left:
                append_list.append(left)
            if right:
                append_list.append(right)

            top = move % self.n if move/self.n > 0 else None
            down = move + self.n if move + self.n < self.n * self.n else None
            if top:
                append_list.append(top)
            if down:
                append_list.append(down)

            left_top = top - 1 if top and top%self.n > 0 else None
            left_down = down - 1 if down and down%self.n > 0 else None
            if left_top:
                append_list.append(left_top)
            if left_down:
                append_list.append(left_down)

            right_top = top + 1 if top and top%self.n < self.n - 1 else None
            right_down = down + 1 if down and down%self.n < self.n - 1 else None
            if right_top:
                append_list.append(right_top)
            if right_down:
                append_list.append(right_down)

            print 'potential list', append_list
            for a in append_list:
                if self.board[a] == self.turn:
                    collection = self.potential_win.get(a)
                    if collection:
                        collection.add(self.turn)
                    else:
                        collection = Set([self.turn])

            self.turn = self.turn * -1

            print 'potential_win:', self.potential_win

    def legal_moves(self):
        return [i for i in range(self.n * self.n) if self.board[i] == 0]

    def game_ends(self, last_move):
        p = self.potential_win.get(last_move)
        if p is not None:
            t = p.get(self.turn * -1) # previous turn
            if t is not None:
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
