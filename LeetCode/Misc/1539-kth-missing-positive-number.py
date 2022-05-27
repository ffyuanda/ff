# https://leetcode.com/problems/kth-missing-positive-number/

# https://leetcode.com/problems/kth-missing-positive-number/discuss/1004535/Python-Two-solutions-O(n)-and-O(log-n)-explained


# This one is actually HARD.

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        beg, end = 0, len(arr)
        while beg < end:
            mid = (beg + end) // 2
            if arr[mid] - mid - 1 < k:
                beg = mid + 1
            else:
                end = mid
        return end + k
