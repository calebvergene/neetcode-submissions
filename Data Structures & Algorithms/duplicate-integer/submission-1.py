class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) < nums:
            return true
        else:
            return false
         