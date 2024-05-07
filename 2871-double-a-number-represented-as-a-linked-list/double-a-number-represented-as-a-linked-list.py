#solution 1 - recursion
#t n 
#s n(stk space)
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