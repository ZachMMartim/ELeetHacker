# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        secondHalf = slow.next
        slow.next = None
        prev = None
        #Reverse second half of the list
        while secondHalf:
            temp = secondHalf.next
            secondHalf.next = prev
            prev = secondHalf
            secondHalf = temp
        
        first, secondHalf = head, prev
        #merge both halves
        while secondHalf:
            temp1, temp2 = first.next, secondHalf.next
            first.next = secondHalf
            secondHalf.next = temp1
            first = temp1
            secondHalf = temp2





        
    
        