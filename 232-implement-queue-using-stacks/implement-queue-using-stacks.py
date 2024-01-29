class MyQueue:

    def __init__(self):
        self.s1 ,self.s2 = [],[]

    def push(self, x: int) -> None:
        
        
        self.s2.append(x)
    

    def pop(self) -> int:
        if self.s1 ==[]:

            while(self.s2):
                x  = self.s2.pop()
                self.s1.append(x)
        return self.s1.pop(-1)

    def peek(self) -> int:
        if self.s1 ==[]:

            while(self.s2):
                x  = self.s2.pop()
                self.s1.append(x)
        return self.s1[-1]

        

        

    def empty(self) -> bool:

        return not(self.s1 or self.s2)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()