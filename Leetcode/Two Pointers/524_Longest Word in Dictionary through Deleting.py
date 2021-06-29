# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/

""" I made some progress lol, I did it in 20 min without an error, something good is
happening, a nice start. Though it's super slow and can only beat 20%, going to optimize it. """

class Solution:
    def findLongestWord(self, s: str, dictionary: list[str]) -> str:
        s_p, d_p = 0, 0
        longest = ""
        for string in dictionary:
            
            while d_p < len(string) and s_p < len(s):
                if s[s_p] == string[d_p]:
                    d_p += 1
                s_p += 1
                
            if d_p == len(string) and len(string) >= len(longest):
                if len(string) > len(longest):
                    longest = string
                else:
                    longest = string if string < longest else longest
            
            s_p, d_p = 0, 0   
            
        return longest


""" for this one, I sorted the dictionary at first and think that it may get faster. It turns out that
I'm wrong, the sorting process takes huge amount of time itself, nah.  """

class Solution:
    def findLongestWord(self, s: str, dictionary: list[str]) -> str:
        s_p, d_p = 0, 0
        longest = ""
        dictionary.sort(key=lambda x: x)
        dictionary.sort(key=lambda x: len(x), reverse=True)        
        
        for string in dictionary:
            
            while d_p < len(string) and s_p < len(s):
                if string[d_p] not in s:
                    break
                    
                if s[s_p] == string[d_p]:
                    d_p += 1
                s_p += 1
                
            if d_p == len(string):
                return string
            
            s_p, d_p = 0, 0   
            
        return longest
                
""" This is the cheapest solution for python. TBH this is disgusting, it is fast yeah
but it uses the find() method which has nothing to do with two pointers, would be meaningless
to use pythonic magic to solve this problem."""

class Solution:
    def findLongestWord(self, s: str, dictionary: list[str]) -> str:
        ans = ""
        for word in dictionary:
            a, b = len(word), len(ans)
            if a < b or (a == b and word > ans): 
                continue
            pos = -1
            for char in word:
                pos = s.find(char, pos + 1)
                if pos == -1: 
                    break
            else:
                ans = word
        return ans
