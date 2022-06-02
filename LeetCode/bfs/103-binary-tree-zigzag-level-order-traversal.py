# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_nodes = []
        
        def bfs(node, level):
            nonlocal level_nodes
            if not node:
                return
            if level > len(level_nodes) - 1:
                level_nodes.append(collections.deque())
            
            if level % 2:
                level_nodes[level].appendleft(node.val)
            else:
                level_nodes[level].append(node.val)

            bfs(node.left, level + 1)
            bfs(node.right, level + 1)

        bfs(root, 0)
        return level_nodes
