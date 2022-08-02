# https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        self.record = []
        def bfs(root, level):
            
            if not root:
                return
            if level > len(self.record):
                self.record.append([])
            
            self.record[level - 1].append(root.val)
            bfs(root.left, level + 1)
            bfs(root.right, level + 1)
        
        bfs(root, 1)
        result = [sum(level) / len(level) for level in self.record]
        return result
