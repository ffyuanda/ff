# https://leetcode.com/problems/squares-of-a-sorted-array/

# Not much to say, utilize the non-descending property

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = count = len(nums) - 1
        output = [0 for _ in range(len(nums))]
                
        while left <= right:
            if abs(nums[left]) < abs(nums[right]):
                output[count] = pow(nums[right], 2)
                right -= 1
            else:
                output[count] = pow(nums[left], 2)
                left += 1
                
            count -= 1
        return output
