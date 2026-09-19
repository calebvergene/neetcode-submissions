class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack_sum(index, combination, curr_sum):
            # check the current combination
            if curr_sum > target:
                return 
            elif curr_sum == target:
                result.append(combination[:])
                return 
            
            # else, then curr_sum still less than target 
            while index < len(nums):
                combination.append(nums[index])
                curr_sum += nums[index]
                backtrack_sum(index, combination, curr_sum)

                # once we return, then we know that what i added didn't work
                curr_sum -= combination.pop()
                index += 1
        
        backtrack_sum(0, [], 0)
        return result
            
