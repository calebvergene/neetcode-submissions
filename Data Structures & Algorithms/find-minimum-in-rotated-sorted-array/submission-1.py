class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            # how can we determine what half the border is?
            elif nums[mid] < nums[0]:
                r = mid - 1
            else:
                l = mid + 1
        