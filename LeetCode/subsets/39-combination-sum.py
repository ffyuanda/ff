# https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        
        def recursion(start, combination, curr_sum):

            if curr_sum == target:
                result.append(combination)
            elif curr_sum > target:
                return

            # loop through candidates (recursion)
            for i in range(start, len(candidates)):
                c = candidates[i]
                
                # Look, we are using i instead of i + 1 here
                # because we *can* have multiple same candidate.
                # And don't worry it will slip into infinity, becasue
                # curr_sum > target above is watching the game.
                recursion(i, combination + [c], curr_sum + c)

        recursion(0, [], 0)
        return result
