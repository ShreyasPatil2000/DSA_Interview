class Solution(object):
    def isValid(self, s: str) -> bool:
        pairs = {"(": ")", "{": "}", "[":"]"}
        stack = []
        for bracket in s:
            if bracket in pairs:
                stack.append(bracket)
            elif len(stack) == 0 or bracket!=pairs[stack.pop()]:
                return False
        return len(stack) == 0        
        
ob = Solution()
print(ob.isValid("()[]{}"))

# We put up all the possible pairs in the dictionary and initialize a stack. We run a for loop for elements in string. Then if it is an opening bracket then we append it. If it is a closing bracket, we compare it to value of key for a popped stack value. If it does not match or if the length of the stack is 0, then we return False. At end, we return if the length of stack is 0.

# Time Complexity: O(N)
# Space Complexity: O(N)
