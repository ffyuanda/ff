# https://leetcode.com/problems/permutations-ii/

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(rlist, temp_list, nums, used, layer=1):
            if len(temp_list) == len(nums):
                rlist.append(copy.copy(temp_list))
                
            else:
                for i in range(len(nums)):
                    # if used[i - 1], that means the previous one is used
                    # somewhere upper level, then we should not continue,
                    # since nums[i - 1] won't be used again down below.
                    # if not used[i - 1], we should continue, because it *will*
                    # be used again down the level.
                    if used[i] or i > 0 and nums[i] == nums[i - 1] and not used[i-1]:
                        print(layer * "-", i, "C", used)
                        continue
                        
                    print(layer * "-", i)
                    used[i] = True
                    temp_list.append(nums[i])
                    backtrack(rlist, temp_list, nums, used, layer + 1)
                    used[i] = False
                    temp_list.pop()
        
        rlist = []
        nums.sort()
        used = [False] * len(nums)
        backtrack(rlist, [], nums, used)
        return rlist
