# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums =  set(nums)

        temp2 = head
        dummy = ListNode()
        temp1 = dummy
        while(temp2):

            if not temp2.val in nums:
                temp1.next  = temp2 
                
                temp1 = temp1.next
                
            temp2 = temp2.next

        temp1.next  = None     



        return dummy.next

        