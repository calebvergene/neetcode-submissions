class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while (l <= r):
            mid = (l+r)//2
            print(nums[l],nums[mid],nums[r])
            if nums[mid] == target:
                return mid
            elif nums[mid] > target and nums[r] >= target and nums[r] > nums[mid]:
                r = mid - 1
            elif nums[mid] > target and nums[r] >= target and nums[r] < nums[mid]:
                l = mid + 1
            elif nums[mid] < target and nums[l] <= target and nums[l] < nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
            
            
        return -1
