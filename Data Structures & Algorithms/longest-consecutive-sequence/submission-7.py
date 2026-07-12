class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ## iterate once thru list with a hash
        ## store each num as a key and make its value its length
        ## its value will be hash[num-1]+1

        hashnum = defaultdict(int)
        for num in sorted(nums):
            if num-1 in hashnum.keys():
                hashnum[num] = hashnum[num-1] + 1
            else:
                hashnum[num] += 1
            print(dict(hashnum))
        return max(hashnum.values())