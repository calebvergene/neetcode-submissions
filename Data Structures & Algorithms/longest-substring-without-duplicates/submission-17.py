class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charhash = {}
        l = 0
        longest = 0
        for i, char in enumerate(s):
            # check if new char in window
            if char in charhash and charhash[char] >= l:
                # if so, set l pointer to after where the old char was
                l = charhash[char] + 1
            charhash[char] = i
            # save max string length 
            longest = max(longest, i - l + 1)
        return longest