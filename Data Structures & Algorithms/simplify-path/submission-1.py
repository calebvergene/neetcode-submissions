class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = [] 
        splitted = path.split('/')
        for chunk in splitted:
            if chunk == "":
                continue 

            if chunk == '..':
                if stack:
                    stack.pop()
                    stack.pop()
                continue
            elif stack == ".":
                continue
            
            stack.append('/')
            stack.append(chunk)
        
        return "/" if not stack else ''.join(stack)
