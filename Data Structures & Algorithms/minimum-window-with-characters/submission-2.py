class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
            
        shortest_substring = s
        chars_remaining = set()
        for char in t:
            chars_remaining.add(char)

        t_hash = defaultdict(int)
        for char in t:
            t_hash[char] += 1
        
        window = defaultdict(int)
        l = 0 
        for r in range(len(s)):
            if s[r] in t_hash:
                window[s[r]] += 1
                if window[s[r]] == t_hash[s[r]]:
                    chars_remaining.remove(s[r])

                # check if we can increment l. only starts when we finished initial substring with all of t. 
                while l < r and not chars_remaining:
                    if s[l] in t_hash and window[s[l]] == t_hash[s[l]]:
                        break # this means we need the l char 
                    window[s[l]] -= 1 
                    l += 1
            
            if not chars_remaining:
                if r - l + 1 < len(shortest_substring):
                    shortest_substring = s[l:r + 1]
        
        return shortest_substring if not chars_remaining else ""


                    


        

