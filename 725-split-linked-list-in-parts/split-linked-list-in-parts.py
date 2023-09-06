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

        #min_number of nodes will be present in each part
        min_nodes  = int(math.floor(tot/  k))
        #in addition to that , the first few number of nodes, will have to accomodare 1 node from the extra nodes, 
        #the number of such nodes having 1 extra node,  is = extr_nodes itself(since each accept on node) 
        max_nodes =  int(math.ceil(tot/  k))
        extra_nodes  = tot- (min_nodes*k)
        temp =head
        pos =1
        while(temp):
            #if else, to see if it  is the part that needs, min_number of nodes, or min_number of nodes+1 
            if pos<=extra_nodes:
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

