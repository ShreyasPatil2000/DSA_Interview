from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        left_arr, right_arr = [1] * N, [1] * N
        left, right, j = 1, 1, 0
        for i in range(N):
            j = -i -1
            left_arr[i] = left
            left *= nums[i]
            right_arr[j] = right
            right *= nums[j]
            
        return [l * r for l, r in zip(left_arr, right_arr)]

ob = Solution()
print(ob.productExceptSelf([1,2,3,4]))

# Assume we added 1 to the left and right side or the list. Create a left array and right array filled with 1s. By iterating through a for loop with a range till length of list, we multiply all the elements on the left side of the position and store it in left list. We do the same for the right side of the position. Then we iterate through both arrays using zip and multiply both values to get the result.

# Time Complexity: O(N) # Iterating through a list takes O(N) and mutliplying values in a zipped list also takes O(N)
# Space Complexity: O(N) # Storing the left_arr values and right_arr values takes O(N) and storing the result also takes O(N) space