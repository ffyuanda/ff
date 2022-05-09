# https://leetcode.cn/problems/employee-free-time/

"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        sorted_schedule = []
        merged = []
        result = []
        
        # pull out every interval and sort them with .start as key
        for each_schedule in schedule:
            for interval in each_schedule:
                sorted_schedule.append(interval)
        sorted_schedule = sorted(sorted_schedule, key=lambda k: k.start)

        # merge these intervals
        for interval in sorted_schedule:
            if merged and merged[-1].end >= interval.start:
                merged[-1].end = max(merged[-1].end, interval.end)
            else:
                merged.append(interval)
        
        # find the "gaps" (common free time) between merged intervals and record them in result
        for i, interval in enumerate(merged):
            if i == 0:
                continue
            if interval.start > merged[i - 1].end:
                result.append(Interval(merged[i - 1].end, interval.start))

        return result
