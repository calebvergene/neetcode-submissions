class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # slow and fast pointer
        slow, fast = 0, 151 % len(nums)
        while nums[slow] != nums[fast] or slow == fast:
            slow = (slow+1) % len(nums)
            fast = (fast +3) % len(nums)
        return nums[slow]
