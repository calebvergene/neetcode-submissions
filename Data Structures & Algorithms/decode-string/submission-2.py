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
                num = ""
                while stack and stack[-1].isnumeric():
                    num += stack.pop()
                num = int(num[::-1])
                repeated *= num
                stack += repeated.split()
                continue
            stack.append(char)
        return "".join(stack)
