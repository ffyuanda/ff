# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        nums = [0] + nums
        
        for i in range(len(nums)):
            index = abs(nums[i])
            nums[index] = -abs(nums[index])
        
        return [i for i in range(len(nums)) if nums[i] > 0]
