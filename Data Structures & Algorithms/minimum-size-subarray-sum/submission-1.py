class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 10 - [1,3,6,4] -> 2

        # once window >= 10, increment left pointer 
        
        l, r = 0, 0
        min_substring = float('inf')
        curr_sum = 0
        while r < len(nums):
            curr_sum += nums[r]
            r += 1
            while curr_sum >= target:
                curr_sum -= nums[l] 
                min_substring = min(min_substring, r-l)
                l += 1
        return min_substring if min_substring != float('inf') else 0
            

