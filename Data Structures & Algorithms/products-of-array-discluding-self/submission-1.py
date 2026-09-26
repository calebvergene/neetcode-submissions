class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixl, prefixr = [1], [1]
        for num in nums:
            prefixl.append(prefixl[-1]*num)
        
        for i in range(len(nums)-1, -1, -1):
            prefixr.append(prefixr[-1]*nums[i])
        prefixr.reverse()
        
        result = [0] * len(nums)
        for i in range(len(nums)):
            result[i] = prefixl[i] * prefixr[i+1]
        return result
