class Node:
    def __init__(self,val):
        
        self.val  = val 
        self.next = None
        
        
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        #dummy node needed for dealing with edge case,   incase the left starts from the head
        dummyHead  = Node(0)
        temp = head 
        ind  = 1
        dummyHead.next = head
        previousNode,nextNode = dummyHead,None
        
        
        while(temp):
        
            #once we reach the node at the left positon , 
            
            #start reversing it
            if ind == left:
                
                prev = previousNode
                next_,curr = temp,temp
                newTail = temp
                while(left<=ind<=right):
                    next_ = curr.next
                    curr.next = prev
                    prev =curr
                    curr= next_
                    ind+=1
                newHead  = prev
                previousNode.next = newHead
                newTail.next=curr
                break

            #previous node keep the node just before the node at left position      
            previousNode = temp
            ind+=1
            temp  = temp.next
        return dummyHead.next 
        
        
        