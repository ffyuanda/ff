# https://leetcode.com/problems/sqrtx/

""" Fuck me this one is so annoying tho it's an easy one. I ignored the fact
that the result can be in the range of [r-1, r+1], so I screwd up a few submissions.
Anyway, it's not hard but the implementation is kinda messy. """

class Solution:
    def mySqrt(self, x: int) -> int:
        upper, lower = x, 0
        result = (upper + lower) / 2
        
        if x == 1: return 1
        
        while upper - lower > 1:
            
            if result*result > x:
                upper = (upper + lower) / 2
                result = (upper + lower) / 2
            elif result*result < x:                
                lower = result
                result = (upper + lower) / 2
            else:
                return int(result)
            
        r = int(result)
        u_r, l_r = r+1, r-1
        if u_r*u_r > x >= r*r: return r
        elif x >= u_r*u_r: return u_r
        elif x < r*r: return l_r
