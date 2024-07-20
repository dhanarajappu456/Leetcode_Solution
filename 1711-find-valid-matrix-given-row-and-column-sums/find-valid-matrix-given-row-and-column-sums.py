class Solution:
    def restoreMatrix(self, rowSum,colSum):
        m, n  = len(rowSum), len(colSum)
        ans  = [[0 for j in range(n)] for i in range(m)] 
        for i in range(m):
            for j in range(n) :
                #update the cell with min value of either the colSum or rowSum for the cell
                val  = min(rowSum[i],colSum[j])
                ans[i][j] = val
                #update the rowSum and colSum 
                rowSum[i]-= val
                colSum[j]-=val
        return ans