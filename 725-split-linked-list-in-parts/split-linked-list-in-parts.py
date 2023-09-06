# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:


        
        ans = [None for i in range(k)]
        tot = 0
        temp = head
        while(temp):
            tot+=1
            temp= temp.next

        #calculate the min number of nodes in each list
        min_nodes  = int(math.floor(tot/  k))
        max_nodes =  int(math.ceil(tot/  k))
        # print(tot, min_nodes)
        extra_nodes  = tot- (min_nodes*k)
        temp =head
        pos =1
        while(temp):
            if pos<=extra_nodes:
                #print(min_nodes, extra_nodes)
                nodes  = min_nodes+1
        
            else:
                nodes  = min_nodes
            dummy = ListNode()
            head =dummy 
            prev =dummy 
            while(temp and nodes):
                
                prev.next=temp
                prev = temp
                temp  = temp.next
                nodes-=1
            prev.next  =None
            ans[pos-1]= head.next
            pos+=1
        return ans 

