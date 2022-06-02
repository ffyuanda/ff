# https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        min_depth = float('inf')
        
        def is_leaf(node):
            return not(node.left or node.right)
        
        def dfs(node, depth):
            nonlocal min_depth
            
            if not node:
                return
            
            if is_leaf(node):
                if depth < min_depth:
                    min_depth = depth
                return
            
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 1)
        return min_depth
