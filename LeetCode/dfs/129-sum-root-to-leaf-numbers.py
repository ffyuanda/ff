# https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def leaf(root):
            return not (root.left or root.right)
            
        def dfs(root, curr_sum):
            
            if not root:
                return
            
            curr_sum *= 10
            curr_sum += root.val
            
            if leaf(root):
                self.res += curr_sum
                
            dfs(root.left, curr_sum)
            dfs(root.right, curr_sum)
            
        dfs(root, 0)
        return self.res