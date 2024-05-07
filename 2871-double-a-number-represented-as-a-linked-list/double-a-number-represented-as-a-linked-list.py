# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rec(root):
            if root == None:
                return 0 
            
            s = root.val*2 + rec(root.next) 
            root.val  = s%10
            c = s//10
            return c 
        
        c = rec(head)
        temp = ListNode(c)
        if c!=0:
            temp.next  = head 
            head = temp
        return head