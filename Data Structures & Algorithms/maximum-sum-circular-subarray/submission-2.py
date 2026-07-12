class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Kadane's algo. 
        # challenge is knowing when to stop if you loop around. 

        max_sum, window = nums[0], 0
        first = 0 # track first index of subwindow 
        end_window = 0

        # first loop, iterate thru the end and find the max sub window
        for i, num in enumerate(nums):
            window += num
            max_sum = max(max_sum, window)
            end_window += num
            if num < 0: # for the end
                end_window = 0
            print(num, window, max_sum)
            if window < 0: # for normal
                window = 0
                first = i
            
        # if you have a positive window by the end of the loop, then you
        # make another loop starting at the front again carrying on the window sum
        # then, stop if you hit a negative window OR the first item in the window. 
        i = 0
        window = max(window, end_window)
        while window > 0 and i != first:
            window += nums[i]
            max_sum = max(max_sum, window)
            i += 1
        
        return max_sum


