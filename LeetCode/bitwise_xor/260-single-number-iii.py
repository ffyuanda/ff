# https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for i in nums:
            xor ^= i
        
        idx = 0
        for i in range(32):
            if xor & (1 << i):
                idx = i
                break
        
        first = 0
        for i in nums:
            if (1 << idx) & i:
                first ^= i
        
        second = first ^ xor
        
        return [first, second]
