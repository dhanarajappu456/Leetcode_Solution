class Solution:
    def restoreMatrix(self, rowSum,colSum):
        m, n  = len(rowSum), len(colSum)
        ans  = [[0 for j in range(n)] for i in range(m)] 
        for i in range(m):
            for j in range(n) :
                val  = min(rowSum[i],colSum[j])
                ans[i][j] = val
                rowSum[i]-= val
                colSum[j]-=val
        return ans