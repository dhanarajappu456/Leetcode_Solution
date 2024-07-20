class Solution:
    def restoreMatrix(self, rowSum,colSum):
        m, n  = len(rowSum), len(colSum)
        ans  = [[0 for j in range(n)] for i in range(m)]
     
        for i in range(m):
            ans[i][0] = rowSum[i]
        for j in range(n):
            col_sm = 0 
            for i in range(m):
                col_sm+= ans[i][j]
                diff =  max(0 , col_sm - colSum[j])
                if diff>0:
                    ans[i][j+1] = diff
                    ans[i][j]-=diff
                col_sm -=diff
        return ans