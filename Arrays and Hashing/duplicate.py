from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate = {}
        for i in nums:
            if i in duplicate:
                return True
            duplicate[i] = 1
        return False
    
ob = Solution()
print(ob.containsDuplicate([1, 2, 3, 4, 1]))

# To solve this problem, we use a dictionary. We initialize an empty dictionary, duplicate, and use a for loop to store the frequency of each number. We introduce a check to determine if any number appears more than once. If no duplicates are found, we return False.

# Time Complexity: O(N), as we iterate through every item in the list.
# Space Complexity: O(N), as we use a dictionary to store up to N items in the worst case, where N is the length of the list.