#coding=utf-8


#记录下一个大于２的数之前的最小的数
def getGoodProfit(prices, p):
    sum = 0
    min_price = prices[0]

    for i in range(len(prices)):
        if prices[i] - min_price > 2:
            sum = prices[i] - min_price -p
            if (i+1)!= (len(prices)-1) :
                min_price = prices[i+1]
            else:
                break
        if prices[i] < min_price:
            min_price = prices[i]


