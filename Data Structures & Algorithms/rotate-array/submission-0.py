class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # k mod, k should be less than len(nums)

        # [1,2,3,4,5,6,7,8], k=3
        k = k % len(nums)
        count = 0 
        
        for first in range(k):
            index = first 
            value = nums[index]
            index = (index + k) % len(nums)
            while index != first:
                # stop this loop if index == first
                # move index to index + k
                temp = nums[index]
                nums[index] = value
                value = temp
                index = (index + k) % len(nums)
                count += 1
            nums[first] = value
            count += 1
            # done with moving each num
            if count == len(nums):
                break
        
        
        
