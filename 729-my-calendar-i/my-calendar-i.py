class TreeNode:
    def __init__(self,start, end) :
        self.left, self.right   = None , None 
        self.s, self.e   = start , end 
        
class MyCalendar:

    def __init__(self):
        
        self.root = None
        
        

    def book(self, start: int, end: int) -> bool:
        
        node = TreeNode(start, end)
        if self.root == None:
            self.root = node
            return True 
        curr   = self.root
        while curr:
            
           
            if curr.e<=start:
                if not curr.right :
                    curr.right  = TreeNode(start, end)
                    return True
                curr = curr.right
                
          
            elif end<= curr.s:
                if not curr.left :
                    curr.left  = TreeNode(start, end)
                    return True
                curr = curr.left
            else:
                return False
        
        
        return True 
            
        
      
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)