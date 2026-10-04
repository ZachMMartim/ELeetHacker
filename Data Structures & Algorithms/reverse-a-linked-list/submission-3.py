# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            #store the pointer
            temp = curr.next
            #This is the reversal
            curr.next = prev
            #Now both Nodes, prev and curr are the same node but curr.next points backwards
            prev = curr
            #Traverse through to the next node
            curr = temp
        
        return prev
