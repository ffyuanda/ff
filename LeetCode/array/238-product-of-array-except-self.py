

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        # get a list of left products and
        # a list of right products:
        #
        #        Numbers:     2    3    4     5
        #        Lefts:       1    2  2*3 2*3*4
        #        Rights:  3*4*5  4*5    5     1
        #
        # The final list of answers is left * right for each number        

        left = 1
        for i in range(n):
            if i > 0:
                left = left * nums[i - 1]            
            res[i] = left
        
        right = 1
        for i in range(n - 1, -1, -1):
            if (i < n - 1):
                right = right * nums[i + 1]
            res[i] *= right
            
        return res
