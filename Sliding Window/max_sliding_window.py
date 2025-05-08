from typing import List
import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap, result = [], []
        for i in range(k):
            heapq.heappush(max_heap, (-nums[i], i))
        result.append(-max_heap[0][0])
        for r in range(k, len(nums)):
            heapq.heappush(max_heap, (-nums[r], r))
            while max_heap[0][1] < (r - k + 1):
                heapq.heappop(max_heap) 
            result.append(-max_heap[0][0])
        return result
            

ob = Solution()
print(ob.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))

# First we initialize max heap and result list. Then we push first k elements into the max heap. We append the max element value to the result. Using a for loop with range k to len(nums). We push each element to the heap. While the max element of heap is out of window, the index is less than (r - k + 1) pop it out. Append the max_heap value to the result and return it.

# Time Complexity: O(NlogN) push and pop operation in heaps is O(LogN) so using loop along with it will make it O(N)
# Space Complexity: O(N) as we are storing the result in an array