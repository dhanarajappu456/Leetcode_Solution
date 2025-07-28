# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        s,f  =  head, head
        while(f and f.next):
            
            s = s.next
            f = f.next.next
            # this condition can't be put at the start of the loop , 
            #cuz, that might include the case where , f and s = is at head , and ther is no cylce
            # but putting this at the start of the loop will say , it has cycle.
            if f==s:
                return True
        return False