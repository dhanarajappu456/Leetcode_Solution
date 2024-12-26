"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        
        def rec(head):

            if head  == None :
                return None
            t1 = rec(head.next)
            t2 = rec(head.child)

            
            if head.child:  
                old_next = head.next 
                head.next  = head.child
                head.child.prev  = head
                
                t2.next  = old_next
                if old_next:
                    old_next.prev  = t2
            head.child    = None 
            
               
            


            return t1 or t2 or head

        rec(head)
        return head
        