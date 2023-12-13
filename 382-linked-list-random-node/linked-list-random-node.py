#solution 1  - hack  create a list and choose a ranodm index

#solution 2- using random sampling- this is a special case of 
#where k = 1 (ie length of reservior)



class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head  = head
    def getRandom(self) -> int:
        res = 0
        count =1 
        temp = self.head
        while(temp!=None):
            if( random.random() < 1/count ):
                res = temp.val
          
            temp = temp.next
            count+=1
        return res


