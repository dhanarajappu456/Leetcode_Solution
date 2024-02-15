'''

map and  prefix sum 

this is problem is similar to the problem , to find the subarray with target k in 1d array 


we store the pref sum for each row. 

for each pair of  start column  c1 and end column  c2  we find each sub matrix starting from the starting row. during this process we find if we can get the sub matrix with c1 as starting col and c2 as ending column  where map is used to store the cumsum of matrices starting from 0th row to current row with c1 and c2 as the ending column


t n^2*m where  ,m,n are the row and column
s mn  - pref array

'''


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m=len(matrix)
        n=len(matrix[0])
        pref =[[0 for i in range(n)] for j in range(m)]
        ans =0 
        for i in range(m):
            prefix_sum =0 
            for j in range(n):
                prefix_sum+= matrix[i][j]
                
                pref[i][j] = prefix_sum
        
    
        
        for c1 in range(n):
            for c2 in range(c1,n):
                mp = {0:1}
                cum_sum = 0 
                for r in range(m):
                    if c1==0:
                        cum_sum+= pref[r][c2]
                    else:
                        cum_sum += pref[r][c2] - pref[r][c1-1]
                        
                    ans+= mp.get(cum_sum - target,0)
                    
                    mp[cum_sum] = mp.get(cum_sum,0)+1
        return ans
                        
                        
                    
                    
                    
        