# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

# Beautiful solution (How recursive!)

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        self.connect_two_nodes(root.left, root.right)
        return root
        
    def connect_two_nodes(self, node1, node2):
        
        if not node1 or not node2:
            return None
        
        node1.next = node2
        self.connect_two_nodes(node1.left, node1.right)
        self.connect_two_nodes(node2.left, node2.right)
        
        self.connect_two_nodes(node1.right, node2.left)
        