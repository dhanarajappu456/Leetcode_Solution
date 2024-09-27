class MyCalendarTwo:

    def __init__(self):
        '''
        keeps two array 
        overlap: keeps only the over lapping section b/w two intervals
        non-ovelap: one keeps all the current interval
        
        so when we are looking for current interval , we can immediately 
        see the overlap , array if there is section(which is already ovelapping b/w two interval) , that overlap with current interval
        
        
        '''
        self.overlap = []
        self.non_overlap = []
        

    def book(self, start: int, end: int) -> bool:
        
        for inter in self.overlap:
            # checks if there is a overlap 
            if start< inter[1]  and end > inter[0]:
                return False
        # this insert the ovelapping section b/w two interval to the overlap array
        for inter in self.non_overlap:
            if start< inter[1]  and end > inter[0]:
                self.overlap.append(( max(start, inter[0]) , min(end, inter[1])))
        #always keep all intervals encountered so far in this list
        self.non_overlap.append((start, end))
        return True
    '''
    t n 
    s n
    '''

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)