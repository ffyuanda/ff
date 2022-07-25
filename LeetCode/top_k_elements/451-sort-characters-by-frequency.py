# https://leetcode.com/problems/sort-characters-by-frequency/

class Solution:
    def frequencySort(self, s: str) -> str:
        counter = collections.Counter(s)
        heap = []
        result = ""
        for val, count in counter.items():
            heapq.heappush(heap, (-count, val))
        
        for _ in range(len(heap)):
            pair = heapq.heappop(heap)
            result += -pair[0] * pair[1]
            
        return result
