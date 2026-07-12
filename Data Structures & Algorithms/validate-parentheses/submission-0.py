class Solution:
    def isValid(self, s: str) -> bool:
        hashs = {')' : '(', '}' : '{', ']' : '['}
        stack = []
        for char in s:
            if char in hashs.values():
                stack.append(char)
            else:
                if stack.pop() == hashs[char]:
                    continue
                else:
                    return False
        if len(stack) == 0:
            return True
        