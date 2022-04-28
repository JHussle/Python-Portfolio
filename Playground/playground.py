def addInterest(balances, rate):
    for i in range(len(balances)):
        balances[i] = balances[i] * (1 + rate)
def test():
    amount = [1000, 2200, 800, 360]
    rate = 0.05
    addInterest(amount, rate)
    print(amount)
test()
        

    
