class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest = 0
        total = 1
        sub = 1
        for i in nums:
            if i == 0:
                total = 1
                sub = 1
            elif i < 0:
                total *= i
                sub = 1
            else:
                sub *= i
                largest = max(largest, sub)
        return max(largest, total)

