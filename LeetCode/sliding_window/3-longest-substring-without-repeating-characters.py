class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        record = dict()
        max_len = 0
        
        left, right = 0, 0
        while right < len(s):

            if s[right] in record:
                # ATTENTION here:
                # using max() here is to prevent regression,
                # namely an input like "abba", if you stick to
                # assign left with record[s[right]] + 1, the 
                # algo moves the left pointer back to an illegal
                # state.
                left = max(left, record[s[right]] + 1)
                
            # keep updating the latest position of each char
            record[s[right]] = right            
            max_len = max(right - left + 1, max_len)
            right += 1
            
        return max_len                
