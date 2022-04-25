# https://leetcode.com/problems/longest-repeating-character-replacement/
# https://leetcode.com/problems/longest-repeating-character-replacement/discuss/91271/Java-12-lines-O(n)-sliding-window-solution-with-explanation/95815

# slightly counter-intuitive one. In this one, we are not actually
# shrinking the window, we are sliding it to the right. Take an example
# "AAABCDAAAAA", with k = 1. Every time max_count changes, the very
# change is accurate, and it also leads to the change of the longest record.
# When we are sliding the window to the right, the current window can be invalid
# until we find another valid and longer window.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = end = 0
        record = collections.Counter()
        max_count = 0
        longest = 0
        
        while end < len(s):
            record[s[end]] += 1
            max_count = max(max_count, record[s[end]])
            
            if end - start + 1 - max_count > k:
                record[s[start]] -= 1
                start += 1
            
            longest = max(longest, end - start + 1)
            end += 1
            
        return longest
