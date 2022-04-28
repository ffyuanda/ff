# https://leetcode.com/problems/sort-colors/

# This is a dutch partitioning problem
# https://en.wikipedia.org/wiki/Dutch_national_flag_problem

# Relative discussion:
# https://leetcode.com/problems/sort-colors/discuss/26481/Python-O(n)-1-pass-in-place-solution-with-explanation

# I feel like this looks a lot like quicksort, using partition technique.

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, len(nums) - 1
        
        while white <= blue:
            
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
                
            elif nums[white] == 1:
                white += 1
                
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
