class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) < len(nums):
            return true
        else:
            return false
         