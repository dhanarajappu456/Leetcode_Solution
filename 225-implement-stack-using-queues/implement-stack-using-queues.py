from collections import deque as dq
class MyStack:

    def __init__(self):

        self.dq1  = dq()
        self.dq2 = dq()
        
    def push(self, x: int) -> None:
        # self.dq.append(x)
        # for i in range(len(self.dq)-1):
        #     self.dq.append(self.dq.popleft())
        if self.dq2:
            self.dq1  = self.dq2
            self.dq2 = []
        self.dq1.append(x)



    
    def pop(self) -> int:
        len_ = len(self.dq1)
        for i in range(len_-1):
            self.dq2.append(self.dq1.popleft())
           
        val  = self.dq1.popleft()
        self.dq1 = self.dq2
        self.dq2 = deque([])
        return val 
        
    def top(self) -> int:
        ans = -1
        len_ = len(self.dq1)
        for i in range(len_):
            val = self.dq1.popleft()
           
            self.dq2.append(val)
            if i ==( len_-1):
                ans   = val
        self.dq1 = self.dq2
        self.dq2 = deque([])
        return ans
        
        
    
    def empty(self) -> bool:
        return len(self.dq1)==0
        
        
