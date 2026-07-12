class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = 0 
        r = 1
        res = []

        while l < len(nums) - 2:
            count = 2
            while r < len(nums) - 1:
                first = nums[l]
                second = nums[r]
                summ = first + second
                r = l + count

                while r < len(nums):
                    if summ + nums[r] == 0:
                        res.append([first, second, nums[r]])
                    r += 1
                count += 1
                r = l + count
            
            l += 1
            r = l + 1

        unique_res = list(map(list, set(res)))
        return unique_res
                
