# https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        def condition(arr, index):
            if arr[index] < arr[index - 1]:
                return True
            return False
        
        left, right = 0, len(arr) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if condition(arr, mid):
                right = mid
            else:
                left = mid + 1
                
        return left - 1
