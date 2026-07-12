class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Kadane's algo. 
        # challenge is knowing when to stop if you loop around. 

        max_sum, window = nums[0], 0
        first = 0 # track first index of subwindow 

        # first loop, iterate thru the end and find the max sub window
        for i, num in enumerate(nums):
            window += num
            max_sum = max(max_sum, window)
            print(num, window, max_sum)
            if window < 0:
                window = 0
                first = i
            
        # if you have a positive window by the end of the loop, then you
        # make another loop starting at the front again carrying on the window sum
        # then, stop if you hit a negative window OR the first item in the window. 
        i = 0
        while window > 0 and i != first:
            window += nums[i]
            max_sum = max(max_sum, window)
            i += 1
        
        return max_sum


