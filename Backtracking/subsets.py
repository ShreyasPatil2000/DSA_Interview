from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset, result = [], []
        def backtrack(i):
            if i == len(nums):
                result.append(subset[:])
                return
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()
            backtrack(i + 1)
        backtrack(0)
        return result
    
ob = Solution()
print(ob.subsets([1, 2, 3]))

# First we have 2 lists, subset and result and the names are exactly what they mean. In our backtrack function we use 0 as parameter till i == len(nums) as we will have len(nums) levels in the tree. We append the subset if i == len(nums) and return. We append nums[i] and backtrack to next. Then we pop then backtrack again. We will get all possible subsets and return them

# Time Complexity: O(N * 2^N)
# Space Complexity: O(N * 2^N)