class Solution:
    def isValid(self, s: str) -> bool:
        hashs = {')' : '(', '}' : '{', ']' : '['}
        stack = []
        for char in s:
            if char in hashs.values():
                stack.append(char)
            elif char in hashs.keys():
                if stack[-1] == hashs[char]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        if len(stack) == 0:
            return True
        return False
        