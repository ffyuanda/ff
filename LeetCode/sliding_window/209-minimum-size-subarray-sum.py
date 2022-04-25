# https://leetcode.com/problems/minimum-size-subarray-sum/
# intuitive one

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = 0
        target_sum = 0
        min_len = float('inf')

        while right < len(nums):
            target_sum += nums[right]
            
            while target_sum >= target:
                min_len = min(right - left + 1, min_len)
                target_sum -= nums[left]
                left += 1
                
            right += 1
            
        return min_len if min_len != float('inf') else 0
