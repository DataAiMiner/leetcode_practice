# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sum_up = 0
        flag = False
        
        if root:
            if root.left is None:
                flag = False
            elif root.left.left is None and root.left.right is None:
                flag = True
        
            if flag:
                sum_up += root.left.val
            else:
                sum_up += self.sumOfLeftLeaves(root.left)
            
            sum_up += self.sumOfLeftLeaves(root.right)
        
        return sum_up
