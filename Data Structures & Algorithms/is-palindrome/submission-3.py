class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, k = 0, len(s)-1
        while i < len(s) // 2 + 1:
            if not s[i].isalnum():
                i += 1
                continue
            elif not s[k].isalnum():
                k -= 1
                continue 
            if s[i].lower() != s[k].lower():
                return False
            i += 1
            k -= 1
        return True