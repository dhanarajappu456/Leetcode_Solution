# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stk =[]
        temp = head
        while(temp!=None):
            num = temp.val
            while(stk and stk[-1].val<num):
                stk.pop(-1)
            stk.append(temp)
            temp = temp.next
        next_ = None
        while(stk):
            stk[-1].next = next_
            next_= stk[-1]
            stk.pop(-1)
        return next_
        
