
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
        return self.rec(head)
       
        
    def rec(self,head):
        
        if head==None or head.next==None:
            return head
        new_head=self.rec(head.next)
        head.next.next=head
        head.next=None
        return new_head