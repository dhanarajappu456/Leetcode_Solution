class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:


        ans = 0 
        m,n  = len(matrix) , len(matrix[0])
        pref  =[[0 for j  in range(n+1)] for i in range(m+1)]
        #storing pref sum for each row
        for i in range(m):
            pref_sum =0 
            for j in range(n):
                pref_sum+= int(matrix[i][j])
                pref[i+1][j+1]  = pref_sum
        #fixing the left and right edge for the reactangle 
        for c1 in range(n):
            for c2 in range(c1,n):
                area = 0
                #iterate on each row assuming it as horizontal edge
                for  r in range(m): 
                    #checking if the horizontal cells are all 1s
                    #in which case this part added to area
                    if (pref[r+1][c2+1] - pref[r+1][c1]) == (c2-c1+1):
                        area += (c2-c1+1)
                    #else reinitialize the area 
                    else:
                        area =0
                    ans  =max(ans, area)
        return ans



        