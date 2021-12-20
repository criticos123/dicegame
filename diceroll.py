
import numpy as np

def diceroll():

    #initialize first roll of dice
    diceOne=np.random.randint(1,7)
    diceTwo =np.random.randint(1,7)

    sum=diceOne+diceTwo

    return sum