# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.longest = -1
        
        def dfs(root):
            
            if not root:
                return -1
            
            l_length = dfs(root.left) + 1
            r_length = dfs(root.right) + 1
    
            self.longest = max(self.longest, l_length + r_length)
            
            return max(l_length, r_length)
            
        dfs(root)
        return self.longest
