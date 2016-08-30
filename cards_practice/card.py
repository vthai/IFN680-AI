from __future__ import division
import os,sys,inspect
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from IFN680_AIMA.probability import *  
from IFN680_AIMA.logic import *
from IFN680_AIMA.utils import *

kingProb = 1.0/3
notKingProb = 2.0/3

var_names = []
for i in range(0, 3):
    var_names.append('card'+ str(i + 1))

init_value = {}
for variable in var_names:
    init_value[variable] = [True, False]

cards = JointProbDist(var_names, init_value)

events = all_events_jpd(var_names, cards, {})

for event in events:
    countTrue = 0
    for _, value in event.items():
        if value == True:
            countTrue += 1
    if countTrue == 1:
        prob = kingProb
    else:
        prob = 0
    cards[event] = prob

print cards.show_approx()

p_King = enumerate_joint_ask('card1', {}, cards)
print 'P(C1=T) =', p_King[True], ',P(C1=F) =', p_King[False]

p_King = enumerate_joint_ask('card2', {}, cards)
print 'P(C2=T) =', p_King[True], ',P(C2=F) =', p_King[False]

p_King = enumerate_joint_ask('card3', {}, cards)
print 'P(C3=T) =', p_King[True], ',P(C3=F) =', p_King[False]


p_King = enumerate_joint_ask('card1', {'card2':False}, cards)
print 'P(C1=T|C2=F) =', p_King[True], ',P(C1=F|C2=F) =', p_King[False]

p_King = enumerate_joint_ask('card2', {'card1':False}, cards)
print 'P(C2=T|C1=F) =', p_King[True], ',P(C2=F|C1=F) =', p_King[False]

p_King = enumerate_joint_ask('card3', {'card2':False}, cards)
print 'P(C3=T|C2=F) =', p_King[True], ',P(C3=F|C2=F) =', p_King[False]

p_King = enumerate_joint_ask('card1', {'card2':False, 'card3': False}, cards)
print 'P(C1=T|C2=F,C3=F) =', p_King[True], ',P(C1=F|C2=F,C3=F) =', p_King[False]


p_King = enumerate_joint_ask('card3', {'card2':True}, cards)
print 'P(C3=T|C2=T) =', p_King[True], ',P(C3=F|C2=T) =', p_King[False]


