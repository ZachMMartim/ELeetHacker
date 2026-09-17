# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if root is None:
                return 0
            left = height(root.left)
            right = height(root.right)
            return 1 + max(left, right)
        def dfs(root):
            if root is None:
                return True
            leftH = height(root.left)
            print("left", leftH)
            rightH = height(root.right)
            print("right", rightH)
            balanced = True if abs(leftH - rightH) <= 1 else False
            return (balanced and dfs(root.left) and dfs(root.right))
        
        return dfs(root)
        