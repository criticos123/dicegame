#using two 6 six sided dice.keep rolling until you lose

import diceroll as dr

def pass_method():

    #initialize first roll of dice
    numberRolls=[]
    roll=dr.diceroll()
    #firstroll
    if roll==7 or roll==11:
        result="win"
        numberRolls.append(roll)
    elif roll==2 or roll==3 or roll==12:
        result="lose"
        numberRolls.append(roll)
    else:
        result="nothing"
        numberRolls.append(roll)

    while result=="nothing":

        rollTwo=dr.diceroll()

        if rollTwo==7:
            result="lose"
            numberRolls.append(rollTwo)
        elif rollTwo==sum:
            result="win"
            numberRolls.append(rollTwo)
        else:
            result="nothing"
            numberRolls.append(rollTwo)

    return result + " "+ str(numberRolls)
