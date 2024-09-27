class MinStack:

    def __init__(self):
        self.stack = []
        self.ordered = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.ordered or val <= self.ordered[-1]:
            self.ordered.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        if popped == self.ordered[-1]:
            self.ordered.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.ordered[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()