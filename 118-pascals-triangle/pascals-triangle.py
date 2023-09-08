class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal=[[]]*numRows
        for i in range(numRows):
            pascal[i]=[0]*(i+1)
            pascal[i][0],pascal[i][i]=1,1
            
            for j in range(1,i):
                pascal[i][j]=pascal[i-1][j-1]+pascal[i-1][j]
        return(pascal)        
            
            
        