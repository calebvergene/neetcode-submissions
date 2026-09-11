class Solution:
    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]