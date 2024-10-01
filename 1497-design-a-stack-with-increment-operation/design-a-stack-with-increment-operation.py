'''
the idea is to se a array called inc , where value at index idx is 
the value to be increased for all elements from bottom of stack , 
till idx+1 numebr of items .

thus when a pop happens it checks if it need to be incremeneted based 
on its position in stack and the same index position in inc stack where the amount by which to be incremented is placed.

so this is kinda lazy update .

so that the inc operateion can be performed in o(1), as compared to brutre which is k 
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
      