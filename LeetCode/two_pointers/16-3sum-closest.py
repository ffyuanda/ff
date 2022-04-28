# https://leetcode.com/problems/3sum-closest/submissions/

# Just like 3sum, without ruling out duplicates.

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        sum_diff = pow(10, 5)
        closest_sum = 0
        nums.sort()
        
        for left in range(len(nums) - 2):
            mid = left + 1
            right = len(nums) - 1
            
            while mid < right:
                
                curr_sum = nums[left] + nums[mid] + nums[right]
                
                if abs(target - curr_sum) < sum_diff:
                    sum_diff = abs(target - curr_sum)
                    closest_sum = curr_sum
                
                if curr_sum - target > 0:
                    right -= 1
                else:
                    mid += 1

        return closest_sum
