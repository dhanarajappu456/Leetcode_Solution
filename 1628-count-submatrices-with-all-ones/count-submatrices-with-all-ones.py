class Solution:
    def numSubmat(self,mat):

        #create the prefix sum for each row 

        #fixing the left side and right side for rectangle as c1 and c2 as the column 
        #see the number of submatices with in this left and right as boundary


        m,n  =len(mat), len(mat[0])
        pref = [[0 for i in range(n+1)] for j in range(m+1)]
        ans = 0 
        for i in range(m):
            s = 0
            for j in range(n):
                s+= mat[i][j]
                pref[i+1][j+1] = s
       
        for c1 in range(n):

            for c2 in range(c1,n):
                start =0 
                
                ones = pref[start+1][c2+1] - pref[start+1][c1] 
                
                while(start<m):
                    #skip all rows that dont have the c2-c1+1(which is ,length of top and bottom side )number of 1's
                    while((start<m )and (ones!=(c2-c1+1))):
                        start+=1
                        if start<m :
                            ones = pref[start+1][c2+1] - pref[start+1][c1] 
                    end  = start
                    #find the start and end row with c2-c1+1(which is ,length of top and bottom side ) number of 1's
                    if end<m: 
                            ones = pref[end+1][c2+1] - pref[end+1][c1] 
                    while((end < m) and( ones == (c2-c1+1))):
                        ans+= end-start+1
                        end+=1
                        if end<m: 
                            ones = pref[end+1][c2+1] - pref[end+1][c1] 
                    start = end
                
        return ans

            