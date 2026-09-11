class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window 

        # freq map to store counts of chars 
        # if you have two chars over k, iterate forward left pointer 
        # until only one is over k

        maxf, maxc = 0,0
        max_substring = k + 1
        freq = defaultdict(int)

        l, r = 0, 0
        while r < len(s):
            freq[s[r]] += 1
            if freq[s[r]] > maxf:
                maxf = freq[s[r]]
            elif freq[s[r]] == maxf:
                maxc += 1
            while (r-l+1)-maxf > k:
                freq[s[l]] -= 1
                if freq[s[l]] == maxf -1: # == means it just decrease from over k
                    if maxc:
                        maxc -= 1
                    else:
                        maxf -= 1
                l += 1
            r += 1
            max_substring = max(max_substring, r-l)
        return max_substring




