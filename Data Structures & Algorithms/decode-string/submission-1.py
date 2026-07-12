class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char == "]":
                repeated = ""
                while stack[-1] != "[":
                    repeated += stack.pop()
                repeated = repeated[::-1]
                stack.pop()
                num = int(stack.pop())
                repeated *= num
                stack += repeated.split()
                continue
            stack.append(char)
        return "".join(stack)
