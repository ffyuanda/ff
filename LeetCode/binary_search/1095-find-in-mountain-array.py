# https://leetcode.com/problems/find-in-mountain-array/

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        def condition(arr, index):
            if arr.get(index) < arr.get(index - 1):
                return True                
            return False
        
        def get_mid(left, right):
            return left + (right - left) // 2
        
        left, right = 0, mountain_arr.length() - 1
        top = 0
        
        while left < right:
            mid = get_mid(left, right)
            
            if condition(mountain_arr, mid):
                right = mid
            else:
                left = mid + 1
        
        top = left - 1

        # search left side
        left = 0        
        right = top
        while left < right:
            mid = get_mid(left, right)
            mid_num = mountain_arr.get(mid)
            
            if mid_num == target:
                left = mid
                break
            if mid_num > target:
                right = mid
            else:
                left = mid + 1
        
        if mountain_arr.get(left) == target:
            return left
        
        # search right side
        left = top
        right = mountain_arr.length() - 1
        while left < right:
            mid = get_mid(left, right)
            mid_num = mountain_arr.get(mid)
            
            if mid_num == target:
                left = mid
                break            
            if mid_num < target:
                right = mid
            else:
                left = mid + 1
                
        if mountain_arr.get(left) == target:
            return left
        
        return -1
