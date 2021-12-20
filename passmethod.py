#using two 6 six sided dice.keep rolling until you lose

import diceroll as dr

def pass_method():

    global numberRolls
    numberRolls=[]
    roll=dr.diceroll()
    #firstroll
    if roll==7 or roll==11:
        result="pass"
        numberRolls.append(roll)
    elif roll==2 or roll==3 or roll==12:
        result="dontpass"
        numberRolls.append(roll)
    else:
        result="nothing"
        numberRolls.append(roll)

    #while loop to keep game going until a winer or lsoer is determined
    while result=="nothing":

        rollTwo=dr.diceroll()

        if rollTwo==7:
            result="dontpass"
            numberRolls.append(rollTwo)
        elif rollTwo==sum:
            result="pass"
            numberRolls.append(rollTwo)
        else:
            result="nothing"
            numberRolls.append(rollTwo)

    return result

