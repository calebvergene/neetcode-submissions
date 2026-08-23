class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_perm = collections.defaultdict(int)
        for char in s1:
            s1_perm[char] += 1
        
        l, r = 0, len(s1)

        # create starting perm window for s2
        s2_window = collections.defaultdict(int)
        for i in range(r):
            s2_window[s2[i]] += 1
        if s2_window == s1_perm:
            return True
        
        # start sliding the window
        while r < len(s2):
            s2_window[s2[l]] -= 1
            if s2_window[s2[l]] == 0:
                s2_window.pop(s2[l])
            l += 1
            s2_window[s2[r]] += 1
            r += 1
            if s2_window == s1_perm:
                return True
        
        return False