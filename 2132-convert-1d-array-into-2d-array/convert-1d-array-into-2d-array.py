class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ans  = [ [0 for j in range(n)] for i in range(m) ]
        
        if m*n != len(original):
            return [ ]
        
        curr = []
        for i in range(len(original)):
            num = original[i]
            row = i//n
            col = i%n 
            ans[row][col] = num 
        return ans 
            