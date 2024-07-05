# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
    
        ptr = head
        prev = None
        mn_l, mn_r, mx_l,mx_r = None ,None ,None ,None 
        min_,max_ = float("inf"),-float("inf")
        i=0
        while(ptr):
            if prev and ptr.next and prev.val<ptr.val and ptr.val>ptr.next.val:
                if mx_l == None:
                    mx_l = i
                else:
                    mx_r  = i
                mn_l, mn_r =mn_r, i
            if prev and ptr.next and prev.val>ptr.val and ptr.val<ptr.next.val:
                if mx_l == None:
                    mx_l = i
                else:
                    mx_r = i 
                mn_l, mn_r =mn_r, i
            if mn_l!= None and mn_r!=None :
                min_  = min(min_, mn_r- mn_l)
            
            if mx_l!= None and mx_r!=None :
                max_  = max(max_, mx_r- mx_l)
            prev = ptr 
            ptr = ptr.next
            i+=1 
        if min_ == float("inf"):
            return [-1,-1]
        return [min_, max_]
