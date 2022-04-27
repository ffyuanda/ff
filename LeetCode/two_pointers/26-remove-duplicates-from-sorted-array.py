# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# Two pointers. One slow and one fast. Non-descending is a key point.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        left = right = 0
        for right in range(1, len(nums)):
            if nums[left] != nums[right]:
                left += 1
            nums[left] = nums[right]
        return left + 1
