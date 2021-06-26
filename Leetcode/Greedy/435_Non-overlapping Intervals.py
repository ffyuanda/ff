# https://leetcode.com/problems/non-overlapping-intervals/

""" My approach to use greedy algorithm went on the right track, but some details
are loose, therefore I finally took a look at the solution (not code but ideas) to
solve this one. I used a set to do the interval record, which is fairly stupid, will 
optimize it. """


class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        sorted_i = sorted(
            intervals, key=lambda x: x[1]
        )  # should sort by the end of the interval
        combined_i = set()
        count = 0

        for i in sorted_i:
            overlap_ct = 0
            temp_set = set()

            for j in range(i[0], i[1] + 1):

                if j in combined_i:
                    overlap_ct += 1

                    if overlap_ct >= 2:
                        count += 1
                        break

                else:
                    temp_set.add(j)

            if overlap_ct < 2:
                combined_i = combined_i.union(temp_set)

        return count


""" second approach """
""" This version is way more faster since it is O(n). The previous version
was really unstable since it loop through every interval from start to end, which is
purely dumb. The set union() method above is O(len(s1) + len(s2)), which is also unstable. """

class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        sorted_i = sorted(intervals, key=lambda x: x[1])
        count, prev = 0, sorted_i[0][1]
        
        for i in range(1, len(sorted_i)):
            if sorted_i[i][0] < prev:
                count += 1
            else:
                prev = sorted_i[i][1]
            
        return count
