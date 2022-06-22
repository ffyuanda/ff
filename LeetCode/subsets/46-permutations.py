# https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(rlist, temp_list, nums):
            if len(temp_list) == len(nums):
                rlist.append(copy.copy(temp_list))
                print(temp_list)
            else:
                for i in range(len(nums)):
                    if nums[i] in temp_list: continue

                    temp_list.append(nums[i])
                    backtrack(rlist, temp_list, nums)
                    temp_list.pop()
        
        rlist = []
        backtrack(rlist, [], nums)
        return rlist
