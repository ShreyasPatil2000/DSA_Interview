class MinStack:

    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        minimum = self.getMin()
        if minimum==None or minimum > val:
            minimum = val
        self.stack.append([val, minimum])
        
    def pop(self) -> None:
        self.stack.pop()
        
    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        else:
            return None
        
    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        else:
            return None

obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())  # Expected: -3
obj.pop()
print(obj.top())     # Expected: 0
print(obj.getMin())  # Expected: -2

# Instead of appending an item at once, append item with minimum instead, [val, min_val]. This will give O(1) time complexity to everything.

# Time Complexity: O(1) all functions have the constant time complexity
# Space Complexity: O(N) to store value in stack