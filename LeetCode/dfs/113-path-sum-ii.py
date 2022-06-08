# https://leetcode.com/problems/path-sum-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.stack = []
        self.res = []
        
        def leaf(root):
            return not (root.left or root.right)
            
        def dfs(root, curr_sum):
            
            if not root:
                return
                
            curr_sum += root.val
            self.stack.append(root.val)
            
            if curr_sum == targetSum and leaf(root):
                self.res.append(copy.copy(self.stack))
                
            dfs(root.left, curr_sum)
            dfs(root.right, curr_sum)
            
            self.stack.pop()
            
        dfs(root, 0)
        return self.res
