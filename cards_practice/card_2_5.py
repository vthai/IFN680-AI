from __future__ import division
import os,sys,inspect
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from IFN680_AIMA.probability import *  
from IFN680_AIMA.logic import *
from IFN680_AIMA.utils import *

'''
    There are a set of 5 cards, 2/3 of them can be Kings, they are all face down
'''

kingProb = 1.0/10  # based on n!/(n-k)!k! = 5!/(5-2)!2! = 10

'''
    define variable called Cardi = {True, False} to denote that whether a card is a King or not
    Cardi = True => cardi is a King, Cardi = False => cardi is not a King
'''

var_names = []
for i in range(0, 5):
    var_names.append('Card'+ str(i + 1))

init_value = {}
for variable in var_names:
    init_value[variable] = [True, False]

'''
    Build the joint probability distribution for the 5 cards (without probability, i.e. P(Cardi) not yet Specified)
'''

cards = JointProbDist(var_names, init_value)

'''
    Generate the permutation for all the possible Cardi combination
    example:
        Card1 = False, Card2 = True, Card3 = True, Card4 = False  => denotes the situation that the 2nd and 3rd card are Kings
        Card1 = True, Card2 = False, Card3 = True, Card4 = True  => denotes the situation that the 1st and 3rd card are Kings
    There could also be impossible situations such as:
        Card1 = False, Card2 = True, Card3 = True, Card4 = True  => more then 2 kings
        Card1 = True, Card2 = True, Card3 = True, Card4 = True  => all kings
    These situation are taken care later at the probability assigning stage
'''
events = all_events_jpd(var_names, cards, {})

'''
    probability assigning stage
    only assign probability to permutation that contains two kings, other permutation are consider invalid so P = 0 (i.e. cannot happen)
'''
for event in events:
    countTrue = 0
    
    for _, value in event.items():
        if value == True:
            countTrue += 1
    if countTrue == 2:
        prob = kingProb
    else:
        prob = 0
    cards[event] = prob

assert(cards.is_valid())

print cards.show_approx()

print '\nIs it valid?', cards.is_valid()

'''
    If no card has been flipped, flipping at any position can be a King with a probability of 4/10 = 0.4
'''
print '\nIf no card has been flipped, flipping at any position can be a King with a probability of 4/10 = 0.4'
p_King = enumerate_joint_ask('Card1', {}, cards)
print 'P(C1=T) =', p_King[True], ',P(C1=F) =', p_King[False]

p_King = enumerate_joint_ask('Card2', {}, cards)
print 'P(C2=T) =', p_King[True], ',P(C2=F) =', p_King[False]

p_King = enumerate_joint_ask('Card3', {}, cards)
print 'P(C3=T) =', p_King[True], ',P(C3=F) =', p_King[False]

'''
    If after a card has been flipped and it is not a King, then the probability of any second card flipped being a King is increased
'''
print '\nIf after a card has been flipped and it is not a King, then the probability of any second card flipped being a King is increased'
p_King = enumerate_joint_ask('Card1', {'Card2':False}, cards)
print 'P(C1=T|C2=F) =', p_King[True], ',P(C1=F|C2=F) =', p_King[False]

p_King = enumerate_joint_ask('Card2', {'Card1':False}, cards)
print 'P(C2=T|C1=F) =', p_King[True], ',P(C2=F|C1=F) =', p_King[False]

p_King = enumerate_joint_ask('Card3', {'Card2':False}, cards)
print 'P(C3=T|C2=F) =', p_King[True], ',P(C3=F|C2=F) =', p_King[False]

'''
    If after second card has been flipped and it is still not a King, then the probability of any second card flipped being a King is further increased
'''
print '\nIf after the second card has been flipped and it is still not a King, then the probability of any third card flipped being a King is further increased'
p_King = enumerate_joint_ask('Card1', {'Card2':False, 'Card3': False}, cards)
print 'P(C1=T|C2=F,C3=F) =', p_King[True], ',P(C1=F|C2=F,C3=F) =', p_King[False]

'''
    If after third card has been flipped and it is still not a King, then the probability of any fourth card flipped being a King is definite (P=1)
'''
print '\nIf after the third card has been flipped and it is still not a King, then the probability of any fourth card flipped being a King is definite (P=1)'
p_King = enumerate_joint_ask('Card1', {'Card2':False, 'Card3': False, 'Card4': False}, cards)
print 'P(C1=T|C2=F,C3=F,C4=F) =', p_King[True], ',P(C1=F|C2=F,C3=F,C4=F) =', p_King[False]


print '\nIf a card has been flipped and it is a King, then the probability of any second card flipped being a King is decreased'
p_King = enumerate_joint_ask('Card3', {'Card2':True}, cards)
print 'P(C3=T|C2=T) =', p_King[True], ',P(C3=F|C2=T) =', p_King[False]

print '\nIf two card has been flipped and they are all Kings, then the probability of any third card flipped being a King is none (P=0)'
p_King = enumerate_joint_ask('Card3', {'Card2':True, 'Card4': True}, cards)
print 'P(C3=T|C2=T,C4=T) =', p_King[True], ',P(C3=F|C2=T,C4=T) =', p_King[False]


