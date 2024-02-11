class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        
        
        #Tabulation - basecase to final
        
        
        m,n = len(grid), len(grid[0])
        dir_ = [-1,0,1]
    
        prev = [[-1 for k in range(n) ]for j in range(n)]
        
        
        
        for i in range(n):
            for j in range(n):
                if i==j:
                    prev[i][j] = grid[m-1][i]
                    
                else:
                    prev[i][j]  = grid[m-1][i] +grid[m-1][j]
               
        
        for i in range(m-2,-1,-1):
            
            curr = [ [-1 for k in range(n) ]for j in range(n)]
            
            for j in range(n):
                for k in range(n):
                    
                    # no need to caculate for first row except dp[0][0][-1]
                    if i==0 and not(j==0 and k==n-1):
                        continue
                    max_ = -1*float("inf")
                    
                    for dir1 in dir_: 
                        for dir2 in dir_:
                            
                            if j+dir1<0 or k+dir2<0 or j+dir1>=n or k+dir2>=n:
                                continue
                            else:
                                max_ = max(max_, prev[j+dir1][k+dir2])
                    
                    if j ==k:
                        curr[j][k] = grid[i][j]+max_
                    else:
                        
                        curr[j][k] = max_+grid[i][j] +grid[i][k]
            
            prev= curr        
                   
        return prev[0][-1]
                
                
        
            
            
            
            
            
        