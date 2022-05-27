# https://leetcode.com/problems/first-missing-positive/


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # this nested loop has a time complexity of O(n)
        # CORRECT SLOT will never be changed: for CORRECT SLOT, A[A[i] - 1] always
        # equals to A[i], vice versa (1) 
        # For each swap, the number of CORRECT SLOT increases by at least 1: Position
        # A[A[i] - 1] = A[i] becomes a CORRECT SLOT after swap, and according to (1),
        # this must be a new CORRECT SLOT 
        # The maximum of CORRECT SLOT <= N
        for i in range(n):
            while nums[i] > 0 and nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1
