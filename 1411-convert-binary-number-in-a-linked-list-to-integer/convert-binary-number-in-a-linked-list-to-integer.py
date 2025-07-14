# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        temp = head
        ans = 0 
        while(temp):
            val = temp.val
            ans  = ans *2 + val
            temp  = temp.next
        return ans