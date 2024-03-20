'''The idea is simple 

find the prev node of node a as s   and next node of node b as e 
then connect s to head of list2 and tail of list2 to e

t n 
s 1

'''
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        #creating dummy node
        d= ListNode()
        d.next = list1

        #finding end of second list
        l2_end = list2
        while(l2_end.next):
            l2_end =l2_end.next


        #fiding the prev node of node at a and and next  node of b 
    
        p1= list1 
        prev = d
        curr = list1
        pos=0
        s,e = None,None
        while(pos!=b):
            if pos==a:
                s = prev
            prev = prev.next
            curr =curr.next
            pos+=1
        
        # handling edge case case when a and b are same
        if s == None:
            s = prev
        e =  curr.next
        # joining the prev node of a in list1  to start head of list2 
        # and joining the tail of list2  to next node of node b in list1 
        s.next = list2
        l2_end.next = e
        return d.next
        