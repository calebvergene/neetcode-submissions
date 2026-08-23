class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + ";" + s
        return encoded
    def decode(self, s: str) -> List[str]:
        original = []
        i = 0
        while i < len(s):
            # get length of current string 
            num = 0 
            place = 10
            while s[i] != ";":
                num *= 10
                num += int(s[i])
                i += 1
            i += 1
            original.append(s[i:i+num])
            i += num
        return original
