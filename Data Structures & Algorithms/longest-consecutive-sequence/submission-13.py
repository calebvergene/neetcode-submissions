class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums = set(nums)
        starters = []
        for num in nums:
            if num-1 not in nums:
                starters.append(num)
        
        sequence = 0
        for starter in starters:
            num = starter + sequence
            while num in nums:
                sequence += 1
                num += 1
        
        return sequence
