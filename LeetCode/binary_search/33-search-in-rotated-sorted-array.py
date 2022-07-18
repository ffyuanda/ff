# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(nums, left, right, target):
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid
                else:
                    left = mid + 1
            return left if nums[left] == target else -1
        
        left, right = 0, len(nums) - 1
        mini = None
        
        # rotated
        if nums[right] < nums[left]:            
            # find the minimum
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] < nums[right]:
                    right = mid
                else:
                    left = mid + 1
            mini = left
            
            # search left side
            left_res = binary_search(nums, 0, mini - 1, target)
            if left_res != -1: return left_res
            
            # search right side
            right_res = binary_search(nums, mini, len(nums) - 1, target)
            if right_res != -1: return right_res
        else:
            return binary_search(nums, left, right, target)
        
        return -1
