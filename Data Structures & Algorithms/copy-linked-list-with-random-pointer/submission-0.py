"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #If an old null was null, ensure the copy is also null
        copyMap = {None : None}

        curr = head
        while curr: 
            #Deep copy
            copy = Node(curr.val)
            copyMap[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            #Get the deep copy
            copy = copyMap[curr]
            #Set the pointers for the copied Node
            copy.next = copyMap[curr.next]
            copy.random = copyMap[curr.random]
            curr = curr.next
        
        return copyMap[head]


        
        
        