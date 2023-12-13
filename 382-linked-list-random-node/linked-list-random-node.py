#solution 1  - hack  create a list and choose a ranodm index

#solution 2-  using random sampling- this is a special case of 
#where k = 1 (ie length of reservior)

#this is solution to the followup , that is when list length now known and when additional space not used 



# t n*m (n = num of calls to getrandom, m = len of linked list  )
# s  1





class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head  = head
    def getRandom(self) -> int:
        res = 0
        count =1 
        temp = self.head
        while(temp!=None):
            #we keep the prev element in the reservior iff its prob = (k/k+i)=(1/count) 
            #(here i is count and k=1 )
            #else we need to replace the element
          
            if( random.random() < 1/count ):
                res = temp.val
          
            temp = temp.next
            count+=1
        return res


