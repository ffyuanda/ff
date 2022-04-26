# https://leetcode.com/problems/max-consecutive-ones-iii/

# Same one as the 424

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        one_count = 0
        max_one_count = 0
        max_len = 0
        start = end = 0
        
        while end < len(nums):
            
            one_count += nums[end]
            max_one_count = max(max_one_count, one_count)
            
            if end - start + 1 - max_one_count > k:
                one_count -= nums[start]
                start += 1
                
            max_len = max(max_len, end - start + 1)
            end += 1
            
        return max_len
