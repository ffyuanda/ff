# https://leetcode.cn/problems/inorder-successor-in-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        self.found = False
        self.result = None

        def bfs(root):
            if not root:
                return
            if self.result:
                return

            bfs(root.left)
            if self.result:
                return
            if root.val == p.val:
                self.found = True
            if self.found and root.val > p.val:
                self.result = root
            bfs(root.right)
        
        bfs(root)
        return self.result
