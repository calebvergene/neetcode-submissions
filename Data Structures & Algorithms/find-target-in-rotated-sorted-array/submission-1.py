class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ## need to binary search and get mid. once i get mid compare 
        ## to first element in the list. 
        ## if first element is '
        if nums[0] == target:
            return 0
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif (nums[0] > target and nums[mid] > target) or (nums[0] < target and nums[mid] < target):
                l = mid + 1
            else:
                r = mid - 1
        return -1