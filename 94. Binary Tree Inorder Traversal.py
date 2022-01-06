# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ### RECURSIVE
    # result = []
    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     if root:
    #         self.inorderTraversal(root.left)
    #         self.result.append(root.val)
    #         self.inorderTraversal(root.right)
    #     return self.result
    
    ### ITERATIVE
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr = root
        stack = []
        result = []
        completed = 0
        
        while True:
            if curr is not None:
                stack.append(curr)
                curr = curr.left
            elif stack:
                curr = stack.pop()
                result.append(curr.val)
                curr = curr.right
            else:
                break
        return result
