# https://leetcode.com/problems/unique-binary-search-trees/


# tabulation
class Solution:
    def numTrees(self, n: int) -> int:
        G = [0] * (n + 1)        
        G[0] = G[1] = 1
        
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                G[i] += G[j - 1] * G[i - j]
        
        return G[n]

# memoization
class Solution:
    def numTrees(self, n: int) -> int:
        self.memo = {i:0 for i in range(21)}
        
        def dp(n):
            if n <= 1: return 1
            if self.memo[n]: return self.memo[n]
            for i in range(1, n + 1):
                self.memo[n] += dp(i - 1) * dp(n - i)
            return self.memo[n]
        
        return dp(n)

