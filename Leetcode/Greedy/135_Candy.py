# https://leetcode.com/problems/candy/

""" I didn't figure out this one initially. I finished it by checking the solutions using two lists, one
goes from left to right and the other goes from right to left, to satisfy the two local requirements in
order to yield the global requirements. """


class Solution:
    def candy(self, ratings: list[int]) -> int:

        if len(ratings) == 1:
            return 1

        length = len(ratings)
        candies = 0
        r2l, l2r = [1] * length, [1] * length

        for i in range(1, length):
            # left to right
            if ratings[i] > ratings[i - 1]:
                l2r[i] = l2r[i - 1] + 1

            # right to left
            if ratings[length - i] < ratings[length - i - 1]:
                r2l[length - i - 1] = r2l[length - i] + 1

        for i in range(0, length):
            if r2l[i] > l2r[i]:
                candies += r2l[i]
            else:
                candies += l2r[i]

        return candies
