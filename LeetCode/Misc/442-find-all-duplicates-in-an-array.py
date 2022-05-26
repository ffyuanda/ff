# https://leetcode.com/problems/find-all-duplicates-in-an-array/

# Good old "find all" logic.

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = [0] + nums
        res = []
        for x in nums:
            if nums[abs(x)] < 0:
                res.append(abs(x))
            else:
                nums[abs(x)] *= -1
        return res
