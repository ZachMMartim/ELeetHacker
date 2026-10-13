# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root): 
            if root is None:
                return (True, 0)
            
            left_balanced, leftH = dfs(root.left)
            right_balanced, rightH = dfs(root.right)

            is_balanced = (left_balanced and right_balanced and abs(leftH - rightH) <= 1)

            return is_balanced, 1 + max(leftH, rightH)
        is_balanced, height = dfs(root)
        return is_balanced
        