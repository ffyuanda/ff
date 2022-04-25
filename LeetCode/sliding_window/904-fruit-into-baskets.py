# https://leetcode.com/problems/fruit-into-baskets/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = end = 0
        type_counts_in_window = collections.Counter()
        types = 0
        maxi = 0
        
        while end < len(fruits):
            if type_counts_in_window[fruits[end]] == 0:
                types += 1
            type_counts_in_window[fruits[end]] += 1
            
            while types > 2:
                type_counts_in_window[fruits[start]] -= 1
                if type_counts_in_window[fruits[start]] == 0:
                    types -= 1
                start += 1

            maxi = max(maxi, end - start + 1)
                
            end += 1
            
        return maxi
