class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ## thoughts: sliding window, l is always the first of the char substring
        ## l changes !to the first non char! when there are more than k non chars
        l, r = 0, 1
        longest = 1

        # track how much k has incremented
        k_tracker = 0

        # save next l  
        next_l = 0

        while r < len(s):
            if s[l] != s[r]:
                if k_tracker == 0:
                    next_l = r
                k_tracker += 1
            if k_tracker > k:
                l = next_l
                r = l
                k_tracker = 0
            longest = max(r-l+1, longest)
            r += 1

        return longest
        

        