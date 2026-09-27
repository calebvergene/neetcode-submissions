class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        # three pointer + binary search = O(n^2logn)
        # for 3 pointers, each time move, need to move to new number 
        # for binary search, as soon as you find matching quad, break

        def move_index(index, value, step):
            while index in range(len(nums)) and nums[index] == value:
                index += step
            return index
        
        i = 0 
        while i < len(nums) - 3:
            # 1 pointer too low, continue early 

            l, r = i+1, len(nums)-1
            while l + 1 < r:
                # 3 pointers too low, continue early
    
                l2, r2 = l+1, r-1 # for the binary search
                bs_target = target - nums[i] - nums[l] - nums[r]
                while l2 <= r2:
                    mid = (l2+r2)//2
                    if nums[mid] == bs_target: 
                        res.append([nums[i], nums[l], nums[mid], nums[r]])
                        break
                    elif nums[mid] < bs_target:
                        l2 = mid + 1
                    else:
                        r2 = mid - 1
                # increment / decrement l or r
                if r2 == l: # 3 pointers too high
                    r = move_index(r, nums[r], -1)
                else: # 3 pointers too low or found pair
                    l = move_index(l, nums[l], 1)

            i = move_index(i, nums[i], 1)
        
        return res

