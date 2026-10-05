class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hshs, hsht = defaultdict(int), defaultdict(int)
        for char in s:
            hshs[char] += 1
        for char in t:
            hsht[char] += 1
        return hshs == hsht