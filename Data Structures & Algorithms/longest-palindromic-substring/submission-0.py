class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = s[0]
        for c in range(len(s)):
            for even in [0,1]:
                l, r = c, c + even
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    if r - l + 1 > len(longest):
                        longest = s[l:r+1]
                    l -= 1 
                    r += 1
        
        return longest 
                
