# https://leetcode.com/problems/missing-number/discuss/69791/4-Line-Simple-Java-Bit-Manipulate-Solution-with-Explaination

# a ^ b ^ b = a

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        i = 0

        while i < len(nums):
            xor = xor ^ i ^ nums[i]
            i += 1
            
        return xor ^ i
