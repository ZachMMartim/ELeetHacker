# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr: 
            #Save for traversal
            temp = curr.next
            #Reverse the pointer
            curr.next = prev
            #Reverse the node, head is now prev
            prev = curr
            #Traverse 
            curr = temp

        return prev