# -*- coding: utf-8 -*-
'''
This package defines 
    - an abstract Game class
    - an abstract Player class
    - a Human_player class
    

Created on Sat 20 Aug 2016

@author: f.maire@qut.edu.au
    
    
'''
import math
import timeit

# for python 2 compatibility
try: 
    input = raw_input
except NameError: 
    pass
    

class IllegalMove(Exception):
    pass


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

class Game(object):
    '''
        Abstract class to represent a game (match) between two players.
        An instance of this class manages the history of the moves, 
        the current state of the board, and whose turn it is.
        
        Atributes:        
            self.turn :  color of the next player to move (-1 Black or +1 White)
            self.history : list of the moves playedd so far
    
    '''

    def display(self):
        '''
            Display the current state
        '''
        raise NotImplementedError # could raise a NonImplemented Exception
        
    def clone(self):
        '''
            Make a clone of this game.
            Implematation s
        '''
        raise NotImplementedError
    
    def do_move(self, m, color=None):
        '''
           Perform move 'm' 
           if color == None, 
              put a stone of color 'self.turn' 
              update self.turn
           else:
              add a stone of color 'color' but
              do not update self.turn
        '''
        raise NotImplementedError
        
    def undo_move(self):
        raise NotImplementedError
    
    def is_terminal(self):
        '''
          Return True if the game is over
                 otherwise return False
        '''
        raise NotImplementedError
    
    def legal_moves(self):
        '''
            Return the list of legal moves for the current player
        '''
        raise NotImplementedError
    
    def set_turn(self, c):
        self.turn = c
        
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
        

class Player(object):
    '''
        Abstract player class
        
        Attributes        
            self.color : -1 or +1  
            self.game : own copy of the game
    '''
    def play(self, game, opp_move):
        '''
            Given 'opp_move', the last move of the opponent 
            return a move 
        '''
        raise NotImplementedError
    
    def set_color(self, c):
        self.color = c

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

class Human_player(Player):
    '''
        Allow a user player to play a game at the console
    '''

    def __init__(self, game):
        self.game = game  # player's own private copy of the board

    def play(self, opp_move):
        if opp_move:
            self.game.do_move(opp_move)
        while True:
            # move is an integer specifying the index of the cell played
            m = int(input("Your Move -> "))
            if m not in self.game.legal_moves():
                print ("Error: illegal move")
                continue
            break
        self.game.do_move(m)
        return m    

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

def play(game, player1, player2, verbose = 1):
    ''' 
        Run a game between two players. 
        Can raise IllegalMove exception
        
        PRE:
          - players have been created
    '''
    
    # Create dictionary  color -> player
    assert player1.color == -player2.color
    if player1.color == -1:        
        dict_color_player = {-1:player1, +1:player2}
    else:
        dict_color_player = {-1:player2, +1:player1}
            
    last_move = None
    
    if verbose:
        print ('** Player {} starts **'.format('Black' if game.turn==-1 else 'White'))
        
    while not game.is_terminal():
        # get the next move from current player
        if verbose:
            game.display()
            print ('Player {} to move '.format('Black' if game.turn==-1 else 'White'))
        move = dict_color_player[game.turn].play(last_move)
        #print ("This is ", game.turn, " turn ", game.legal_moves())
        if move not in game.legal_moves():
            raise IllegalMove
        # update the master board
        #print ("Finalize the move", move)
        game.do_move(move)
        last_move = move
        
    # display terminal state
    if verbose:
        print('** Game over **')
        game.display()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


class Minmax_player(Player):
    '''
    A player that uses minmax to computes its moves.
    
    Attributes:
        self.maxply : depth of the lookahead (default is 2)
        self.eval_fn : the evaluation function to use at the leaves        
    '''

    def __init__(self, game, eval_fn = lambda x : 0):
        self.game = game  # player's own copy of the board
        self.maxply = 3 # 
        self.eval_fn = eval_fn  # default evaluation function

    def play(self, opp_move):
        print ("AI thinking...")
        '''
            Return a move using the minmax algorithm
            
            PRE:
                Game state not terminal        
        '''                
        if opp_move >= 0:
            self.game.do_move(opp_move)
        
        start = timeit.default_timer()
        best = None # pair  (value, move)
        # try each move
        for m in self.game.legal_moves():
            #print ("Try this step", m)
            self.game.do_move(m)
            
#“INSERT YOUR CODE HERE”
            
            #val = self.min(self.maxply - 1)
            val = self.minimax_value_prune(self.maxply - 1, -math.inf, math.inf)
            #val = self.minimax_value(self.maxply - 1)

            if best is None or val > best[0]:
                best = (val, m)
            #print ("Revert step")
            self.game.undo_move()

        end = timeit.default_timer()
        print("timer =", (end - start))

        m = best[1] # best move found
        
        # need to play this move on our own copy of the board
        print ("AI choose", m)
        self.game.do_move(m)
        return m

    def max(self, maxply):
        #print ("Calling max for ", maxply)
        if maxply == 0 or self.game.is_terminal():
            return self.eval_fn(self.game)

        best_val = -math.inf
        for m in self.game.legal_moves():
            self.game.do_move(m)
            val = self.min(maxply - 1)
            if best_val is None or val > best_val:
                best_val = val
            self.game.undo_move()
        #print ("Max choose ", best_val)
        return best_val

    def min(self, maxply):
        #print ("Calling min for ", maxply)
        if maxply == 0 or self.game.is_terminal():
            return self.eval_fn(self.game)

        best_val = math.inf
        for m in self.game.legal_moves():
            self.game.do_move(m)
            val = self.max(maxply - 1)
            if best_val is None or val < best_val:
                best_val = val
            self.game.undo_move()
        #print ("Min choose ", min_m)
        return best_val

    
    def minimax_value_prune(self, maxply, alpha, beta):
        """Find the utility value of the game state w.r.t. the current player."""
      
        # if we have reached the maximum depth, the utility is approximated
        # with the evaluation function
        if maxply == 0 or self.game.is_terminal():
            return self.eval_fn(self.game)
    
        best_val = None # just a value, not a move
    
        # try each move
        for m in self.game.legal_moves():
            from_opponent = (self.game.turn == -1)
            self.game.do_move(m)
#“INSERT YOUR CODE HERE”
            val = self.minimax_value_prune(maxply - 1, alpha, beta)
            if from_opponent: # opponent => min player
                if best_val is None or val < best_val:
                    beta = math.inf if best_val == None else best_val
                    best_val = val
            else: # AI => max player
                if best_val is None or val > best_val:
                    alpha = -math.inf if best_val == None else best_val
                    best_val = val
            
            if alpha >= beta:
                self.game.undo_move()
                return alpha if from_opponent else beta

            self.game.undo_move()

        return best_val

    def minimax_value(self, maxply):
        """Find the utility value of the game state w.r.t. the current player."""
      
        # if we have reached the maximum depth, the utility is approximated
        # with the evaluation function
        if maxply == 0 or self.game.is_terminal():
            return self.eval_fn(self.game)
    
        best_val = None # just a value, not a move
    
        # try each move
        for m in self.game.legal_moves():
            from_opponent = (self.game.turn == -1)
            self.game.do_move(m)
#“INSERT YOUR CODE HERE”
            val = self.minimax_value(maxply - 1)
            if from_opponent: # opponent => min player
                if best_val is None or val < best_val:
                    best_val = val
            else: # AI => max player
                if best_val is None or val > best_val:
                    best_val = val

            self.game.undo_move()

        return best_val





