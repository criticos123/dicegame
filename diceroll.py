
import numpy as np

def diceroll():

    #initialize roll of dice
    diceOne=np.random.randint(1,7)
    diceTwo =np.random.randint(1,7)
    
    #need sum of two dices to play craps
    sum=diceOne+diceTwo

    return sum