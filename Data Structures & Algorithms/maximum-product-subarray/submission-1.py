class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_window, last_window = nums[0], 1
        # either going to be whole array (if even negatives)
        # or a subarray (if odd negatives)
        total = 1

        # solution: either going to be product of whole array, nums[:last negative], or nums[first negative:]
        # total will by default find nums[:last negative] if it updates max each turn
        # so now last_window can track [first negative:]
        negative_found = False
        for num in nums:
            if negative_found:
                last_window *= num
            if num < 0:
                negative_found = True
            total *= num
            max_window = max(max_window, total)
        
        return max(max_window, last_window)
