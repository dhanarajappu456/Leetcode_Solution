# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy =ListNode(-700)
        temp = dummy
        curr = head
        while(curr):
            if temp.val!= curr.val:
                print("fkdj")
                temp.next = curr
                temp = temp.next
              
            curr = curr.next
            temp.next = None
        
        return dummy.next     
          