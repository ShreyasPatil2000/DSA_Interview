from typing import List

class Solution:  
  # def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
  #       numMap = {}
  #       pairs = []
  #       for num in nums:
  #           if target - num in numMap:
  #               pairs.append([target - num, num])
  #           numMap[num] = True
  #       return pairs

  #   def threeSum(self, nums: List[int]) -> List[List[int]]:
  #       triplets = set()  # Use a set to store unique triplets
  #       nums.sort()

  #       for i in range(len(nums) - 2):
  #           if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates for i
  #               continue
            
  #           pairs = self.twoSum(nums[i + 1:], -nums[i])
  #           for pair in pairs:
  #               triplets.add(tuple([nums[i]] + pair))  # Convert triplet to tuple and add to set

  #       return [list(triplet) for triplet in triplets]  # Convert triplets set back to list of lists

  def threeSum(self, nums: List[int]) -> List[List[int]]:
    N = len(nums)
    nums.sort()
    result = []
    for i in range(N - 2):
      if nums[i] == nums[i - 1] and i > 0:
        continue
      left, right = i + 1, N - 1
      while left < right: 
        total = nums[left] + nums[right] + nums[i]
        if total < 0:
          left += 1
        elif total > 0:
          right -= 1
        else:
          result.append([nums[i], nums[left], nums[right]])
          left += 1
          right -= 1
          while left < right and nums[left] == nums[left - 1]:
            left += 1
          while left < right and nums[right] == nums[right + 1]: 
            right -= 1
    return result
      
ob = Solution()
print(ob.threeSum([-1, 0, 1, 2, -1, -4]))

# This is really similar to two sum sorted algorithm. We initialize an empty result list. First we sort the numbers and then record length in N. We iterate through a for loop with range being N-2 as we want the last 3 values to be i, left, right. if i > 0 and nums[i] = nums[i-1] we continue to the next number. We total the amount in while loop checking if left is less than right. If total is less than 0, we increase left. If total is greater than 0 then we increase the right. If total is equal to 0, we append it to the result and adjust left and right. In while loop we check for nums[left] = nums[left - 1] or nums[right] = nums[right + 1] and adjust pointers again. At the end, we return the result. 

# Time Complexity: O(N**2) We have sorting which is O(NlogN) There are 2 loops so O(N**2)
# Space Complexity: O(N**2) We are appending triplets in 2D list. This is in worst case. K is the number of unique triplets 