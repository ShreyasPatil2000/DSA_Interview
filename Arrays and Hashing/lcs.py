from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        left, k, N = 0, 1, len(nums)
        maxlen = 1
        if(N<2):
            return k
        while(left < N-1):
            if nums[left]+1 == nums[left+1]:
                k += 1
            else:
                k = 1
            maxlen = max(maxlen, k)
            left += 1
        return maxlen

ob = Solution()
print(ob.longestConsecutive([100, 4, 200, 1, 3, 2]))

# This is the easiest way to solve this but not the most optimzied solution. First, we take a set of nums and convert to list to make it iterable. Then if length of the list is less than 2 then we return it. We then run a while loop and check whether left is less than N-1 as the last element of left should be N-1 to terminate. We then compare the number at left pointer added by 1 to the next position and check if they are equal. Then we increment our counter by 1. If they aren't equal we set counter back to 1. On every iteration, we check for the maxlen of the sequence using max and increment the left pointer

# Time Complexity: O(NlogN) It is because of using sort method and the loop itself takes O(N)
# Space Complexity: O(N) We are storing list of set of nums back in nums which is causing this, maxlen itself only takes O(1) space