# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        out = []
        for curr in sorted(intervals, key=lambda i: i[0]):
            
            if out and out[-1][1] >= curr[0]:
                out[-1][1] = max(out[-1][1], curr[1])
            else:
                out.append(curr)
        
        return out
