'''solution2 - 
monotonic stk  of  decreasing value
t n 
s n 
'''
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stk =[]
        temp = head
        while(temp!=None):
            num = temp.val
            #whenever current node val>all previus node, we remove those nodes
            while(stk and stk[-1].val<num):
                stk.pop(-1)
            stk.append(temp)
            temp = temp.next
        next_ = None
        while(stk):
            stk[-1].next = next_
            next_= stk[-1]
            stk.pop(-1)
        return next_
        
