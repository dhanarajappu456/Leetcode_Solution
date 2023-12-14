class Solution:

    def __init__(self, n: int, blacklist: List[int]):

        self.white_len   = n  - len(blacklist) 

        self.whites_to_move = []
        for i in range(self.white_len, n):
            if i not in blacklist:
                self.whites_to_move.append(i)

        j = 0
        self.mapping ={}
        for i in blacklist:
            if i<self.white_len:
                self.mapping[i] =self.whites_to_move[j]
                j+=1
        


        
    def pick(self) -> int:

        val = random.randint(0,self.white_len-1)
        if val in self.mapping:
            return self.mapping[val]
        return val
