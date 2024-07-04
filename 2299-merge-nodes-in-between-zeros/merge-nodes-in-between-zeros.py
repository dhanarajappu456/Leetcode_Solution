# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        ()
        '''
        dummy = ListNode()
        tmp = dummy
        prev = None
        ptr = head
        while(ptr):
            if ptr.val == 0:
                tmp.next = ListNode(0)
                prev = tmp
                tmp = tmp.next
            else:
                tmp.val+=ptr.val

            ptr = ptr.next
        prev.next = None
        return dummy.next
        