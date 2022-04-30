# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

# Nice and easy two-pointers, finally learned to sort the list first
# though I highly doubt this is O(nlogn) ... Amortized O(n)?


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        
        si, sj = 0, len(nums) - 1
        i, j = 0, len(nums) - 1
        i_found = j_found = False
        
        while i < j:
            if not i_found and sorted_nums[si] == nums[i]:
                i += 1
                si += 1
            else:
                i_found = True
            
            if not j_found and sorted_nums[sj] == nums[j]:
                j -= 1
                sj -= 1
            else:
                j_found = True
            
            if i_found and j_found:
                break
                
        return j - i + 1 if i_found and j_found else 0
