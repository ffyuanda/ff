# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.largest = float('-inf')
        
        def dfs(root):
            
            # exit condition
            if not root:
                return 0
            
            # recursively find the left and right child's maxPathSum
            l_val = dfs(root.left)
            r_val = dfs(root.right)
            
            left_sum = l_val + root.val
            right_sum = r_val + root.val
            both_sum = l_val + r_val + root.val

            # find out the maximum path sum for this node
            # only 4 possibilities here
            # take both left and right, only left, only right, or only root itself.
            path_sum = max(both_sum, left_sum, right_sum, root.val)
    
            # update max sum
            self.largest = max(self.largest, path_sum)
            
            # only 3 possibilities here
            # take only left, only right, or only root itself (it cannot take
            # both left and right, because that does not satisfy a `path` for
            # this root's parent)
            return max(left_sum, right_sum, root.val)
            
        dfs(root)
        return self.largest
