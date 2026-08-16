class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        lowest = 101
        for day in prices:
            if day < lowest:
                lowest = day
            else:
                profit = max(profit, day-lowest)
        return profit