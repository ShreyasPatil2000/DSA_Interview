import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]       

obj = KthLargest(3, [4, 5, 8, 2])
print(obj.add(3))
print(obj.add(5))
print(obj.add(10))
print(obj.add(9))
print(obj.add(4))

# We initialze heap and k in init method. In add, we push new value into the heap. We use a while loop to pop till length of heap is greater than k.

# Time Complexity: O(m log N + N) where N is the heapify time complexity and m = len(nums) - k and log N is time complexity of popping element from heap
# Space Complexity: O(N) as we store the heap 