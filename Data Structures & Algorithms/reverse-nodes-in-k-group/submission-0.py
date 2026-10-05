# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        #Save one node right before the next group
        tail = dummy

        while True:
            kthNode = self.getKth(tail, k) 
            if not kthNode:
                break
            nextNode = kthNode.next

            #reverse group
            prev, curr = kthNode.next, tail.next

            while curr != nextNode:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            #temp is the first node of the next group
            temp = tail.next
            tail.next = kthNode
            tail = temp
        return dummy.next
            



    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr



        