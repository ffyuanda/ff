# https://leetcode.com/problems/ipo/

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap = []
        
        # sort non-descendingly using capital
        projects = sorted(zip(profits, capital), key=lambda l: l[1])
        i = 0
        
        for _ in range(k):
            while i < len(projects) and projects[i][1] <= w:

                # push to make a max heap (largest profit stays on top)
                heapq.heappush(heap, -projects[i][0])
                i += 1
            
            # pop out the largest profit
            if heap: w -= heapq.heappop(heap)
                
        return w
    