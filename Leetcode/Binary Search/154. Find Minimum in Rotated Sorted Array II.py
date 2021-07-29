# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

""" Quite similar to 81, and I've learned this way of solving problem. """

class Solution:
    def findMin(self, nums: list[int]) -> int:
        
        start = 0
        end = len(nums) - 1

        while start <= end:
            
            if nums[start] < nums[end]:
                # has not been rotated
                return nums[start]

            mid = (start + end) // 2

            if nums[mid] > nums[start]:
                # mid in F array
                start = mid + 1
                
            elif nums[mid] < nums[start]:
                # mid in S array
                if nums[mid-1] > nums[mid]:
                    return nums[mid]
                end = mid - 1
                
            else:
                # cannot determine
                start += 1
                continue
                
        return nums[mid]
        