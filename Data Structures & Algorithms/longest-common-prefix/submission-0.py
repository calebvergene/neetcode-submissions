class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = strs[0]
        index = 0 
        while index < len(word):
            for w in strs:
                if w[index] != word[index]:
                    return word[:index]
            index += 1
        return word