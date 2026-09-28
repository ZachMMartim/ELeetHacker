# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result = []

        queue = deque()
        queue.append(root)

        while queue:
            currLevel = []
            queueLen = len(queue) 
            for i in range(queueLen):
                currNode = queue.popleft()
                currLevel.append(currNode.val)
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
            result.append(currLevel)
            
        return result

        