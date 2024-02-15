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
                        
                        
                    
                    
                    
        