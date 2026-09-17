# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #Main thing to look for is whether subtree starting from subroot exists in the main tree starting from root
        def dfs(root):
            if root is None:
                return False
            if containsSubroot(root, subRoot):
                return True

            return dfs(root.left) or dfs(root.right)

        def containsSubroot(root, subroot):
            if root is None and subroot is None:
                return True
            if root is None or subroot is None:
                return False
            if root.val != subroot.val:
                return False
            
            return containsSubroot(root.left, subroot.left) and containsSubroot(root.right, subroot.right)

        if subRoot is None:
            return True

        return dfs(root)
        