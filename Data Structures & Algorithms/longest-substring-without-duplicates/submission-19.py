class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hsh = {}
        l, r = 0, 0 
        mx = 0
        while r < len(s):
            char = s[r]
            if char in hsh and hsh[char] >= l:
                l = hsh[char] + 1
            hsh[char] = r
            r += 1
            mx = max(mx, r-l)
        return mx


