
from collections import defaultdict as dict 
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
   
        map_  ={None:None}
        curr = head
        while curr:
            
            #creating the copy of current (original node) if not present
            if curr not in map_:
                
                map_[curr] =  ListNode(curr.val)
                
           
            
           # create copy of curr.next node , if not present
            if curr.next not in map_:
                
                map_[curr.next] = ListNode(curr.next.val)
            
         
           # create copy of curr.random node , if not present    
            if curr.random not in map_:
                
                map_[curr.random] = ListNode(curr.random.val)
                
            # linking the next and random nodes  int copy linked list
            
            copy = map_[curr]
            copy.next =  map_[curr.next]
            copy.random  =map_[curr.random]
        
        
            curr = curr.next
        #return the head of the copied linked list
        return (map_[head])                          
       
        
        