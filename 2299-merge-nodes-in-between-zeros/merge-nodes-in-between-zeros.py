# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        
        '''
        ptr  =  head
        dummy =ListNode()
        temp = dummy 
        while(ptr):
            if (ptr.next!=None) and(ptr.val == 0) :
                temp.next = ptr
                temp = temp.next
            else:
                temp.val+= ptr.val

                
            ptr = ptr.next
        # remove unnecessary nodoe to right of temp
        temp.next = None
        return dummy.next