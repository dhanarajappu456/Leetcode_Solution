class Solution:
    def numSubmat(self,mat):

        #create the prefix sum for each row 

        #fixing the left side and right side for rectangle as c1 and c2 as the column 
        #see the number of submatices with in this 


        m,n  =len(mat), len(mat[0])
        pref = [[0 for i in range(n)] for j in range(m)]
        ans = 0 
        for i in range(m):
            s = 0
            for j in range(n):
                s+= mat[i][j]
                pref[i][j] = s
        # print(pref)
        for c1 in range(n):

            for c2 in range(c1,n):
                start =0 
                
                ones = pref[start][c2] - (pref[start][c1-1] if c1-1>= 0  else 0 )
                #skip all rows that dont have the c2-c1+1 number of 1's
                while(start<m):
                    while((start<m )and (ones!=(c2-c1+1))):
                    
                        start+=1
                        if start<m :
                            ones = pref[start][c2] - (pref[start][c1-1] if c1-1>= 0  else 0 )
                        
                    end  = start
                    #find the start and end row with c2-c1+1 number of 1's
                    if end<m: 
                            ones = pref[end][c2] - (pref[end][c1-1] if c1-1>= 0  else 0 )
                
                    while((end < m) and( ones == (c2-c1+1))):
                        #print("inner",c1,c2, start,end)
                        ans+= end-start+1
                        end+=1
                        if end<m: 
                            ones = pref[end][c2] - (pref[end][c1-1] if c1-1>= 0  else 0 )
                    start = end
                
                # print(c1,c2,ans)
        return ans

            