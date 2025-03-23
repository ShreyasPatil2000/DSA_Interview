from typing import List

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        addition = {}
        for index, num in enumerate(nums):
            if target-num in addition:
                return [addition[target-num], index]
            addition[num] = index


ob = Solution()
print(ob.twoSum([2,7,11,15], 9))

# In 2 sum, we have a list and a target. We are trying to find and return the indexes of numbers in the list that can sum up to the target. We don't return all possible combinations but the first possible combination in the list. We take a dictionary let's say addition and we iterate through the nums list using enumerate where index is the index of the elements in the list and num is the element in num.

# Time Complexity: O(N) as we are only iterating through a dictionary
# Space Complexity: O(N) to store the items in the dictionary