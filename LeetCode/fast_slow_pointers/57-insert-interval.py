# https://leetcode.com/problems/insert-interval/

# Just insert and merge

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        out = []
        no_out = [newInterval]
        if not intervals:
            return no_out
            
        for i, v in enumerate(intervals):
            
            if newInterval[0] <= v[0]:
                intervals.insert(i, newInterval)
                break
            if i == len(intervals) - 1:
                intervals.append(newInterval)
                break
                
        for i, v in enumerate(intervals):
            
            if out and out[-1][1] >= v[0]:
                out[-1][1] = max(out[-1][1], v[1])
            else:
                out.append(v)        
        
        return out
