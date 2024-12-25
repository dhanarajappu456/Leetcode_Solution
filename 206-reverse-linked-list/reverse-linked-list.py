
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
       
        
        def rec(head):
            
            if head == None or head.next == None:
                return head
            
            nw_head  =rec(head.next)
            head.next.next  = head 
            head.next = None
            return nw_head
        
        return rec(head)