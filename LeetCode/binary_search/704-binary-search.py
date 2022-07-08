# https://leetcode.com/problems/binary-search/

# template:
# https://leetcode.com/discuss/general-discussion/786126/Python-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems

# rules:
# 1. set up the boundary to include all possible elements
# 2. after exiting the while loop, left is the minimal k​ satisfying the
#    condition function
def binary_search(array) -> int:
    def condition(value) -> bool:
        pass

    left, right = min(search_space), max(search_space) # could be [0, n], [1, n] etc. Depends on problem
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left



class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)
        mid = 0
        
        while low < high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid
            else:
                low = mid + 1
        return -1
