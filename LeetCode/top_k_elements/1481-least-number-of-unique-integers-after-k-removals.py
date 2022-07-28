# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = collections.Counter(arr)
        heap = []
        
        for (value, count) in counter.items():
            heapq.heappush(heap, (count, value))
        
        while k > 0:
            pair = heapq.heappop(heap)
            # count
            if pair[0] <= k:
                k -= pair[0]
            else:
                return len(heap) + 1

        return len(heap)
