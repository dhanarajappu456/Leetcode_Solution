# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        t1 , t2 = l1 , l2
        dummy  = ListNode()
        temp = dummy
        carry = 0 
        while(t1 or t2 or carry):
            a, b  = 0,0
            if t1:
                a = t1.val
            if t2:
                b = t2.val
            s = a + b + carry
            carry = s//10
            rem = s%10
            
            #use either of the nodes in the first or second linked list ,
            #rather than creating another  , until necessary
            node  =  None
            if t1:
                node  = t1
            elif t2:
                node = t2
            else:
                node  = ListNode()

            node.val  = rem 
            temp.next = node
            temp  = node
            if t1:
                t1  = t1.next
            if t2:  
                t2 = t2.next
        
        return dummy.next



        