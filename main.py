import betting as bt
import passmethod as pm

cash=int(input("How much cash would you like to play: "))
bet=int(input("How much cash would you like to bet: "))

result=pm.pass_method()

while result=="nothing":
    result=pm.pass_method()

bt.betting(result,cash,bet)
print(str(pm.numberRolls))



    

