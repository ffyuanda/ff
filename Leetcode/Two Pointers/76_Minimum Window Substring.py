# https://leetcode.com/problems/minimum-window-substring/

""" This solution results in TLE. Need to optimize the time complexity. """

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right = 0, 0
        temp_t = t
        min_sub = s
        least = False
        
        if len(t) > len(s): 
            return ""
        if len(t) == len(s):
            for i in t:
                if i not in s:
                    return ""
        
        while left < len(s):        
            
            if len(temp_t) == 0: # found the substring
                least = True
                temp_t = t
                sub = s[left:right]
                
                if len(sub) < len(min_sub):
                    min_sub = sub

                for i in range(left + 1, right):
                    if s[i] in t:
                        left, right = i, i
                        break
            
            if right >= len(s):
                break
            
            if s[right] in temp_t:
                ti = temp_t.index(s[right])
                temp_t = temp_t[:ti] + temp_t[ti + 1:]

            right += 1

        if least: 
            return min_sub
        else:
            return ""
        

""" Modified version. This ver is from Leetcode's solution, I've read through it and learned about the
algorithm behind, but I'm too tired at this point to reinvent it. So I'll leave it here and realize it
later during review."""

from collections import Counter
class Solution:
    def minWindow(self, s, t):

        if not t or not s:
            return ""

        # Dictionary which keeps a count of all the unique characters in t.
        dict_t = Counter(t)

        # Number of unique characters in t, which need to be present in the desired window.
        required = len(dict_t)

        # left and right pointer
        l, r = 0, 0

        # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
        # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these conditions are met.
        formed = 0

        # Dictionary which keeps a count of all the unique characters in the current window.
        window_counts = {}

        # ans tuple of the form (window length, left, right)
        ans = float("inf"), None, None

        while r < len(s):

            # Add one character from the right to the window
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1

            # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            # Try and contract the window till the point where it ceases to be 'desirable'.
            while l <= r and formed == required:
                character = s[l]

                # Save the smallest window until now.
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                # The character at the position pointed by the `left` pointer is no longer a part of the window.
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

                # Move the left pointer ahead, this would help to look for a new window.
                l += 1    

            # Keep expanding the window once we are done contracting.
            r += 1    
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
