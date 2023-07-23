#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # nested for loop O(n^2)
        '''max_profit = 0
        for buy in range(len(prices)-1):
            for sell in range(buy+1, len(prices)):
                profit = prices[sell] - prices[buy]
                if profit > max_profit:
                    max_profit = profit'''

        # one pass O(n)
        buy = 0
        sell = 1
        max_profit = 0

        while sell < len(prices):
            profit = prices[sell] - prices[buy]
            if profit > max_profit:
                max_profit = profit

            elif profit <= 0:
                buy = sell

            sell += 1

        return max_profit




# @lc code=end

