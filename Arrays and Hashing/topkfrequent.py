from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        heap, result = [], []
        for i in nums:
            counter[i] = counter.get(i, 0) + 1
        for key, value in counter.items():
            heapq.heappush(heap, (-value, key))
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return result
    
ob = Solution()
print(ob.topKFrequent([1,1,1,2,2,3, 3, 3, 3, 3], 2))

# Whenever we have top k or kth largest or anything related to k, we use heap or priority queue. First, we count the frequency of all elements in the list. We take the key, value pairs in tuple form and push them into the heap by making the value negative. This is done because heap is a minimum heap by default and there is no option to initialize a max heap. After that, we append the 1st element of the popped heap tuple to the result. This stores the key that has the max frequency in order.

# Time Complexity: O(NlogN) as pushing in heap is log(N) complexity and iterating for loop along with push is Nlog(N) and iterating for loop with pop is Klog(N) so approximately Nlog(N)
# Space Complexity: O(N) to store result list