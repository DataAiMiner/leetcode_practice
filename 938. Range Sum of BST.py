# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sum = 0
    def searchTree(self, tree: Optional[TreeNode], low, high):
        if tree.val:
            if tree.val >= low and tree.val <= high:
                self.sum += tree.val
            if tree.left is not None:
                self.searchTree(tree.left, low, high)
            if tree.right is not None:
                self.searchTree(tree.right, low, high)
    
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.searchTree(root, low, high)
        return self.sum
