# https://leetcode.com/problems/unique-binary-search-trees-ii/

# You need to figure out that the connect(low, high) returns
# a list of all unique BSTs, with each of them has a root value
# between low to high. Or to say, all the unique BSTs can be formed
# using root values from low to high.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:        
        
        # connects and add the BSTs ranged from low to high
        def connect(low, high):
            res = []          
            
            if low > high:
                res.append(None)
                return res
                        
            for i in range(low, high+1):
                left_tree = connect(low, i-1)
                right_tree = connect(i+1, high)
                
                for left in left_tree:
                    for right in right_tree:
                        
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        res.append(root)
            return res
        
        return connect(1, n)