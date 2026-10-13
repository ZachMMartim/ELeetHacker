# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        longest = float("-inf")
        
        def dfs(root):
            nonlocal longest
            currentSum = float("-infinity")
            if root is None:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            currentSum = (root.val + max(0, left) + max(0, right))
            longest = max(longest, currentSum)
            return root.val + max(0, left, right)
        dfs(root)
        return longest
        