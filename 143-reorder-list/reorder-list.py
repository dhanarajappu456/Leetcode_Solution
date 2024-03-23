
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        start = head
        mid =  self.findMid(head)
        last  = self.reverse(mid)
        dummy = ListNode(0)
        temp = dummy 
        
        p1,p2=head,last
        while(p2):
            #if p1 and p2 same then knitt it via p2 only
            if p1!=p2: 
                temp.next = p1
                temp = temp.next
                p1 = p1.next
            
            temp.next=p2
            temp= temp.next
            p2 = p2.next
             
        return dummy.next
            
        
    def findMid(self,root):
        slow   = root
        fast =  root
        while(fast and fast.next):
            fast = fast.next.next
            slow =slow.next
        return slow
    
    def reverse(self,root):
        prev ,curr,next_ = None, root,root
        while(curr):
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        return prev
            
            
            