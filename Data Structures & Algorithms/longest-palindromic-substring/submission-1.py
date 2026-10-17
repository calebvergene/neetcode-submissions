class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = s[0]
        for c in range(len(s)):
            for even in [0,1]:
                l, r = c, c + even
                distance_needed = len(longest) - (r-l+1) + 1
                distance_needed += distance_needed%2
                distance_needed = distance_needed // 2
                checkl, checkr = l - distance_needed, r + distance_needed
                if checkl < 0 or checkr >= len(s) or s[l] != s[r]:
                    continue

                while l >= 0 and r < len(s) and s[l] == s[r]:
                    if r - l + 1 > len(longest):
                        longest = s[l:r+1]
                    l -= 1 
                    r += 1
        
        return longest 
                

# longest = aaaaa odd, need 3
# longest = bbbbbb even, need 3