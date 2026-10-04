# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Have 2 pointers spaced out by n
        #Create a dummy node to start from head.prev
        #dummy.next = head
        #dummy.val = 0
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0 and right: 
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next
        
        #delete the nth from end node
        left.next = left.next.next

        return dummy.next



        