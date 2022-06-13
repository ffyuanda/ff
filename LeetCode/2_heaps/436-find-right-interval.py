# https://leetcode.com/problems/find-right-interval/

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        record = {item[0]: index for index, item in enumerate(intervals)}
        output = [-1 for i in range(len(intervals))]
        
        heap_start = []
        heap_end = []
        
        for i in intervals:
            heapq.heappush(heap_start, (i[0], i))
            heapq.heappush(heap_end, (i[1], i))
            
        while heap_end and heap_start:
            
            # find right interval
            left = heap_end[0][1]
            right = heap_start[0][1]

            if right[0] >= left[1]:
                heapq.heappop(heap_end)
                r_index = record[right[0]]
                l_index = record[left[0]]
                output[l_index] = r_index
            else:
                heapq.heappop(heap_start)

        return output
