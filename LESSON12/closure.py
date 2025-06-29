# Closure is a funtion that has the scope(parms) of its parent 
# after its parent return
def parent(parm, coin=3):
    # coin = 3 also works
    def child():
        nonlocal coin
        coin-=1
        if coin>1:
            print(f'\n{parm} has {coin} coins left')
        elif coin==1:
            print(f'\n{parm} has {coin} coin left')
        else:
            print(f'\n{parm} is out of coins')
    return child

tommy = parent('Tommy', 3)
jenny = parent('Jenny', 5)

tommy()
tommy()

jenny()
