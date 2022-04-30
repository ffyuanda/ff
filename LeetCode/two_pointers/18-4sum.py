# https://leetcode.com/problems/4sum/

# Hated N-sum problems, but I finally grabbed it...
# They can all be converted to 2-sum using recursion.

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def find_n_sum(nums, N, target, cur):
            if len(nums) < N or N < 2 or nums[0] * N > target or nums[-1] * N < target:
                return
            
            if N == 2:                
                l, r = 0, len(nums) - 1
                
                while l < r:
                    curr_sum = nums[l] + nums[r]
                    if curr_sum > target:
                        r -= 1                        
                    elif curr_sum < target:
                        l += 1
                    else:
                        result.append(cur + [nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1                            
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
            else:
                for i in range(len(nums) - N + 1):
                    if i == 0 or nums[i] != nums[i - 1]:
                        find_n_sum(nums[i + 1 :], N - 1, target - nums[i], cur + [nums[i]])
    
        result = []
        find_n_sum(sorted(nums), 4, target, [])
        return result
