# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
       
        def rec(root):
            
            if root  == None:

                return  -1, None
            max_,nxt = rec(root.next)
            if root.val>=max_:
                root.next = nxt
                return root.val,root
            else:
                return max_,nxt

        return rec(head)[1]