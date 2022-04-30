# https://leetcode.com/problems/backspace-string-compare/

# Gee... Cannot believe this is 'Easy'. The gist here
# is to iterate reversely.


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def get_next_valid_index(s, index):
            
            backspace_count = 0
            while index >= 0:
                if s[index] == "#":
                    backspace_count += 1
                elif backspace_count > 0:
                    backspace_count -= 1
                else:
                    break
                    
                index -= 1
            return index
                
        i = len(s) - 1
        j = len(t) - 1
        
        while i >= 0 or j >= 0:
            
            i1 = get_next_valid_index(s, i)
            j1 = get_next_valid_index(t, j)
            
            if i1 < 0 and j1 < 0:
                return True
            
            if i1 < 0 or j1 < 0:
                return False
            
            if s[i1] != t[j1]:
                return False
            
            i = i1 - 1
            j = j1 - 1
            
        return True
            