class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        bestprofit = 0
        buy = prices[0]
        for price in prices:
            profit = price - buy
            if profit > bestprofit:
                bestprofit = profit
            if price < buy:
                buy = price
        return bestprofit
