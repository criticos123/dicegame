
def betting(result,cash,bet):

    if result=="pass":
        cash=cash+bet
    elif result=="dontpass":
        cash=cash-bet

    if cash<=0:
        result="you have no cash left"

    print(result+" "+str(cash))

