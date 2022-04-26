# https://leetcode.com/problems/find-all-anagrams-in-a-string/

# This one is exactly the same as the 567
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        output = []
        counter = Counter(p)
        match = 0
        w = len(p)
        
        for i in range(len(s)):
            
            if s[i] in counter:
                if not counter[s[i]]: match -= 1
                counter[s[i]] -= 1
                if not counter[s[i]]: match += 1
            
            if i >= w and s[i-w] in counter:
                if not counter[s[i-w]]: match -= 1
                counter[s[i-w]] += 1
                if not counter[s[i-w]]: match += 1
            
            if match == len(counter):
                output.append(i-w+1)
                
        return output
