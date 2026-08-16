class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        lowest = 101
        for day in prices:
            ## set new lowest day 
            if day < lowest:
                lowest = day 
            profit = max(profit, day - lowest)

        return profit