class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = [] # only tracks minimum elements

    def push(self, val: int) -> None:
        self.stack.append(val)
        # handle adding min to empty stack
        min_val = float('inf') if not self.minstack else self.minstack[-1]
        # new min, push to minstack
        # <=, keep duplicates
        if val <= min_val:
            self.minstack.append(val)

    def pop(self) -> None:
        # pop min, pop minstack
        popped = self.stack.pop()
        if popped == self.minstack[-1]:
            self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
