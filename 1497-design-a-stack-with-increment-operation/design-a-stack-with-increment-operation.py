'''
'''
class CustomStack:
    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        self.inc = [0 for i in range(maxSize)]
        

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if self.stack == []:
            return -1
        top_ind = len(self.stack)-1
        
        
        incr_val  = self.inc[top_ind]
        self.inc[top_ind] = 0
        if top_ind - 1>=0:
            self.inc[top_ind-1] += incr_val
        return self.stack.pop() + incr_val
        
            

    def increment(self, k: int, val: int) -> None:
        idx = min(k,len(self.stack))-1
        if idx>=0:
            self.inc[idx] += val
      