class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in [']', '}', ')']:
                if not stack: # more closing than opening 
                    return False 
                if char == ']' and stack.pop() != '[':
                    return False
                elif char == '}' and stack.pop() != '{':
                    return False
                elif char == ')' and stack.pop() != '(':
                    return False
            else:
                stack.append(char)
        
        return not stack