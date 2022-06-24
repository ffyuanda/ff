# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtrack(opening, closing, s):
            nonlocal result
            if closing > opening or opening > n:
                return
            
            if opening + closing == n * 2:                
                result.append("".join(s))
                return

            s.append('(')
            backtrack(opening + 1, closing, s)
            s.pop()

            s.append(')')
            backtrack(opening, closing + 1, s)
            s.pop()
        
        backtrack(0, 0, [])
        return result
