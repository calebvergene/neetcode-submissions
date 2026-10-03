class Solution:
    def execute(self, op, num1, num2):
        if op == "+":
            return num2 + num1
        elif op == "-":
            return num2 - num1
        elif op == "*":
            return num2 * num1
        return num2 / num1

    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []
        for token in tokens:
            try:
                token = int(token)
                numbers.append(token)
            except:
                num1, num2 = numbers.pop(), numbers.pop()
                numbers.append(int(self.execute(token, num1, num2)))
        return numbers[0]
