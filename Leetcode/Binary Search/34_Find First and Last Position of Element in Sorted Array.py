# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

""" Remember how to write the binary search method! """

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        lower, mid, upper = 0, 0, len(nums)-1
        found = False

        while lower <= upper:
            
            mid = (lower + upper) // 2
            if nums[mid] > target:
                upper = mid - 1
            elif nums[mid] < target:
                lower = mid + 1
            else:
                found = True
                break
                
        if found:
            left, right = mid, mid
            while True:
                if left < 0 or nums[left] != target:
                    break
                left -= 1
            while True:
                if right >= len(nums) or nums[right] != target:
                    break
                right += 1
            return [left+1, right-1]
        else:
            return [-1, -1]
        