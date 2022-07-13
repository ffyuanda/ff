# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        left, right = 0, len(nums) - 1
        start = end = 0
        
        if not nums:
            return [-1, -1]
        
        while left < right:
            
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left = mid
                break
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
                
        if nums[left] != target:
            return [-1, -1]
        
        for i in range(left, -1, -1):
            if nums[i] != target:
                start = i + 1
                break
        for i in range(left, len(nums) + 1):
            if i > len(nums) - 1:
                end = len(nums) - 1
                break
            if nums[i] != target:
                end = i - 1
                break
                
        return [start, end]
