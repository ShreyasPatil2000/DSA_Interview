from typing import List

class Solution: 
    def trap(self, height: List[int]) -> int:
        result = 0
        n = len(height)
        height = [0] + height + [0]
        leftmax = [0] * (n + 2)
        rightmax = [0] * (n + 2)
        for i in range(1, n):
            leftmax[i] = max(leftmax[i - 1], height[i - 1])
        for i in range(n - 1, -1, -1):
            rightmax[i] = max(rightmax[i + 1], height[i + 1])
        for i in range(1, n):
            water = min(leftmax[i], rightmax[i]) - height[i]
            if water > 0:
                result += water
        return result
    
ob = Solution()
print(ob.trap([4, 2, 0, 3, 2, 5]))

# We add 0 to each side of the height array. We initialize 2 arrays leftmax and rightmax to store maximum height at each position using loop. In another loop we compare the minimum between them and subtract the height to get the amount of water there. If the water is greater than 0, then we add it to the result and return it.

# Time Complexity: O(N) as we are using 3 for loops of O(N) each, the assignments in the loops only take O(1) time
# Space Complexity: O(N) as we have to calculate water and add for each height, but in worst case all nodes may have water.