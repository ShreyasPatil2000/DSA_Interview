from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        maxarea = 0
        left, right = 0, n - 1
        while left < right:
            area = (right - left) * min(height[left], height[right])
            maxarea = max(area, maxarea)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxarea


ob = Solution()
print(ob.maxArea([1,8,6,2,5,4,8,3,7]))

# First we take the length of the list as n. We initialize 2 pointers left=0 and right= n-1. In a while loop where left < right, we calculate the area. Then we check for maxarea. We compare height[left] and height[right] and we wanna keep the height which has a larger value so we move pointers respectively.

# Time Complexity: O(N) Each pointer is moving n times
# Space Complexity: O(1) The result is constant space