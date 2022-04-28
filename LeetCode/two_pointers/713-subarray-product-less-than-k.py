# https://leetcode.com/problems/subarray-product-less-than-k/

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        prod = 1
        count = 0
        
        for right in range(len(nums)):
            
            prod *= nums[right]
            
            while prod >= k and left <= right:
                prod /= nums[left]
                left += 1
            
            # By intuition, every time the legal window increase,
            # the length of the window amount of possibilities are added.
            count += right - left + 1
            
        return count
