class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window 

        # freq map to store counts of chars 
        # if you have two chars over k, iterate forward left pointer 
        # until only one is over k

        above_k = set()
        max_substring = k + 1
        freq = defaultdict(int)

        l, r = 0, 0
        while r < len(s):
            freq[s[r]] += 1
            if freq[s[r]] > k:
                above_k.add(s[r])
            while len(above_k) > 1:
                freq[s[l]] -= 1
                if freq[s[l]] == k: # == means it just decrease from over k
                    above_k.remove(s[l])
                l += 1
            r += 1
            max_substring = max(max_substring, r-l)
        return max_substring




