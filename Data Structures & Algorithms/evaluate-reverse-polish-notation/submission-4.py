class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tokens.reverse()
        
        def evaluate_top_3():
            num1, num2 = int(tokens.pop()), int(tokens.pop())
            op = tokens.pop()
            if op == "+":
                tokens.append(str(num1+num2))
            elif op == "-":
                tokens.append(str(num1-num2))
            elif op == "*":
                tokens.append(str(num1*num2))
            else:
                tokens.append(str(num1//num2))

        while len(tokens) > 1:
            evaluate_top_3()
        
        return int(tokens[0])