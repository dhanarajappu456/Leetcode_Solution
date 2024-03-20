# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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
        #strored in s and e 
        p1= list1 
        prev = d
        curr = list1
        pos=0
        s,e = None,None
        while(pos!=b):
            if pos==a:
                print(pos,a)
                s = prev
         
            prev = prev.next
            curr =curr.next
            pos+=1
        if s == None:
            s = prev
        e =  curr.next
        s.next = list2
        l2_end.next = e
        return d.next
        