class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s.split()) == sorted(t.split()):
            return True
        return False