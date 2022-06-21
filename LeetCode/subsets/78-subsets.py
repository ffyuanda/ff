# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        
        def backtrack(rlist, temp_list, nums, start):
            rlist.append(copy.copy(temp_list))
            
            for i in range(start, len(nums)):
                temp_list.append(nums[i])
                backtrack(rlist, temp_list, nums, i + 1)
                temp_list.pop()
    
        rlist = []                
        # nums.sort()
        backtrack(rlist, [], nums, 0)
        return rlist
