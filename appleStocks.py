# How much money I could have made yesterday if I'd been trading Apple stocks all day. Write an
# efficient function that takes prices & returns the best profit I could have made from one 
# purchase and one sale of one share of Apple stock yesterday.
def max_profit(stockprices):
# Approach: We need to track the maximum profit and lowest price at each step by using a 
# greedy algorithm. We need to check if: 1) We can get a better profit by buying at minimum price
# and selling at the current price. 2) we have a new minimum price.
# Initialization: 1. minprice = the first price of the day -> stockprices[0]
# 2. maxprofit = first profit we could get -> stockprices[1]-stockprices[0]
# if we buy at the first time and sell at the second time, we need stockprices to have at least
# 2 values:
    if len(stockprices)<2:
        print("At least 2 prices are needed to get the profit")
# In addition, we need to make sure we are always buying at an earlier price and never at the
# current price-don't buy and sell at time 0
    minprice = stockprices[0]
    maxprofit = stockprices[1] - stockprices[0]
    for currentprice in stockprices[1:]:
        profit = currentprice - minprice
        maxprofit = max(maxprofit,profit)
        minprice = min(minprice,currentprice)
    
    return maxprofit

stockprices = [10,7,5,8,11]
print(max_profit(stockprices))