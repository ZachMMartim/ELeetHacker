# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        DFS function will return whether the subtree of the main tree contains the subroot
        """

        def isSameTree(rootA, rootB):
            if rootA is None and rootB is None:
                return True
            if rootA is None or rootB is None:
                return False
            if rootA.val != rootB.val:
                return False

            return isSameTree(rootA.left, rootB.left) and isSameTree(rootA.right, rootB.right)
            
        def dfs(root):
            if root is None:
                return False
            if isSameTree(root, subRoot):
                return True
            return dfs(root.left) or dfs(root.right)

        return dfs(root)

