# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        

        carry = 0
        #if the end has an 8+7, there is still a carry that we need to account for
        while l1 or l2 or carry: 
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            #Compute current digit
            val = v1 + v2 + carry
            #Get new carry if exists
            carry = val // 10
            #Give us the ones place digit
            val = val % 10
            curr.next = ListNode(val)

            #update pointers
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


            
        
        


        