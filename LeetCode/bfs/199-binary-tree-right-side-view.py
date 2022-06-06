# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.result = []
        
        def bfs(root, level):
            
            if not root:
                return None
            
            if level > len(self.result):
                self.result.append(None)
            
            if not self.result[level - 1]:
                self.result[level - 1] = root.val
            
            bfs(root.right, level + 1)            
            bfs(root.left, level + 1)
                
        bfs(root, 1)
        return self.result
