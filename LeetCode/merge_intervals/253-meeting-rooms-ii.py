# https://leetcode.cn/problems/meeting-rooms-ii/

# This one is actually merge interval, it just doesn't 
# look like one. I realize that intervals with the structure [start, end]
# can be devided and sorted into two lists: a list for starts, a list for ends.

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        events = [(iv[0], 1) for iv in intervals] + [(iv[1], -1) for iv in intervals]
        events.sort()
        ans = cur = 0

        for _, e in events:
            cur += e
            ans = max(ans, cur)
        return ans
