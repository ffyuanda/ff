# https://leetcode.com/problems/merge-sorted-array/

""" First attempt, way too slow, gonna optimize it. """
""" Wait, I reran the code and it beats 90.28%, WTF? """

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = 0, 0
        while p2 < len(nums2):
            if nums1[p1] <= nums2[p2] and m > 0:
                p1 += 1
                m -= 1
            else:
                nums1.pop()
                nums1.insert(p1, nums2[p2])
                p1 += 1
                p2 += 1
