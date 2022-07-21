# https://leetcode.com/problems/complement-of-base-10-integer/

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        
        if n == 0: return 1
        
        mask = ~0
        while mask & n:
            mask = mask << 1
        
        return ~n ^ mask
