# https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        heap = []
        result = []
        for val, count in counter.items():
            heapq.heappush(heap, (-count, val))
        
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
            
        return result
