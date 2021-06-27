# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

""" I failed the time constraint at the first attempt coz I tried to brute force it with a O(n^2) comp.
Later I discovered that the given condition "sorted" is of some usage and therefore I can use two pointers, one
from left, another from right, to traverse the whole list. Need to learn the way to prove the correctness of 
an algorithm later from the Intro."""

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1
        
        while True:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
