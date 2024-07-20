class Solution:
    def restoreMatrix(self, rowSum,colSum):
        m, n  = len(rowSum), len(colSum)
        ans  = [[0 for j in range(n)] for i in range(m)]
        #sufficing the row 
        for i in range(m):
            ans[i][0] = rowSum[i]
        
        #cheking if the cols_sum is satisified , if not move the values to the next row
        for j in range(n):
            col_sm = 0 
            for i in range(m):
                col_sm+= ans[i][j]
                diff =  max(0 , col_sm - colSum[j])
                #if there is an excess than the given colSum for the col, then move the excess
                #to the cell in the next col of the same row .
                if diff>0: 
                    #removing the excess value 
                    ans[i][j]-=diff
                    #moving the excess to the cell of next col and same row 
                    ans[i][j+1] = diff
                col_sm -=diff
        return ans