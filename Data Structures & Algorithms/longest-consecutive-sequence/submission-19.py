class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        longest = 1
        nums = set(nums)
        for num in nums:
            if num - 1 not in nums:
                cur = 1
                i = 1
                while num + i in nums:
                    cur += 1
                    i += 1
                longest = max(longest, cur)
        return longest