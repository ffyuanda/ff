# https://leetcode.com/problems/assign-cookies/
class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        cookies = 0
        pointer = 0

        for i in range(len(s)):
            if pointer >= len(g):
                break
            if s[i] >= g[pointer]:
                cookies += 1
                pointer += 1
        return cookies
