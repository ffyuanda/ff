# https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        self.result = False
        if not root:
            return self.result
        
        def leaf(root):
            return not (root.left or root.right)
            
        def dfs(root, curr_sum):
            
            if self.result:
                return
            
            if not root:
                return
                
            curr_sum += root.val
            
            if curr_sum == targetSum and leaf(root):
                self.result = True
                
            dfs(root.left, curr_sum)
            dfs(root.right, curr_sum)
            
        dfs(root, 0)
        return self.result
