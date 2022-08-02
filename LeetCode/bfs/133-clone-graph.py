# https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        self.visited = {}
                
        # dfs here makes and returns a perfect copy of node
        def dfs(node):
            
            history_n = self.visited.get(node.val, False)
            if history_n:
                return history_n
            
            copy_node = Node(node.val)
            self.visited[node.val] = copy_node
            
            for n in node.neighbors:
                copy_n = dfs(n)
                copy_node.neighbors.append(copy_n)
            
            return copy_node
        
        if not node:
            return None
        
        if node.neighbors:
            return dfs(node)
        else:
            return Node(node.val)
