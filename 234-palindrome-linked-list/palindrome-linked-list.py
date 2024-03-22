# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head ==None and head.next==None:
            return True
        
        middle = self.middle(head)
        middle.next=self.reverse(middle.next)
        temp=middle.next 
        while(temp):
            if temp.val!=head.val:
                return False
            temp=temp.next
            head=head.next
            
        return True    
        
    
    def middle(self,head):
        fast=head
        slow=head
        while(fast.next and fast.next.next):
            fast=fast.next.next
            slow= slow.next
        return slow
    def reverse(self,head):
        
        prev=None
        curr,next_=head,head 
        while(curr):
            next_=curr.next
            curr.next=prev
            prev=curr
            curr=next_
        return prev    
        
    
    
        