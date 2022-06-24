# https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []

        def backtrack(s, index, char_list):
            nonlocal result
            
            if len(char_list) == len(s):
                result.append("".join(char_list))
                return
            
            if s[index].isalpha():
                char_list.append(s[index])
                backtrack(s, index + 1, char_list)
                char_list.pop()
                
                if s[index].isupper():
                    s_mod = s[index].lower()
                else:
                    s_mod = s[index].upper()
                char_list.append(s_mod)
                backtrack(s, index + 1, char_list)
                char_list.pop()
            
            else:
                char_list.append(s[index])
                backtrack(s, index + 1, char_list)
                char_list.pop()
                
        backtrack(s, 0, [])
        return result
