class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # make a hash of starting numbers 
        # then make nums a set 
        # then find longest sequence

        # init
        numhash = {}

        for num in nums:
            numhash[num] = 1
        
        for num in numhash:
            if num-1 not in numhash:
                # then its a starter number
                while num + numhash[num] in numhash:
                    numhash[num] += 1
        
        return max(numhash.values())
