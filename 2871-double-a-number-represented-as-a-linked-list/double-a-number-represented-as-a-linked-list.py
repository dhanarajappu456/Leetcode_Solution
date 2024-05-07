#solution 1 - using stack
#t n 
#s n
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stk  = []
        temp  = head
        while(temp):    
            stk.append(temp)
            temp =temp.next
        c = 0
        while(stk):
            node = stk.pop()
            v = node.val*2 + c
            node.val  = v%10
            c = v//10
        temp = ListNode(c)
        if c :
            temp.next  = head
            head  = temp
        return head