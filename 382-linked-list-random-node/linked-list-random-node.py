#solution 1  - hack  create a list and choose a ranodm index

class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.li =[]
        ptr = head
        while(ptr):
  
            self.li.append(ptr.val)
            ptr = ptr.next
    def getRandom(self) -> int:
        ind = random.randint(0,len(self.li)-1)
        return self.li[ind]


