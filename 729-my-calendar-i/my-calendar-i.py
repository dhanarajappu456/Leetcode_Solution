class MyCalendar:

    def __init__(self):
        
        self.mp = set()
        

    def book(self, start: int, end: int) -> bool:
        
        for e in  self.mp: 
            
            if not(end <=e[0]  or e[1] <=start):
                return False
            
        self.mp.add( ( start, end))
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)