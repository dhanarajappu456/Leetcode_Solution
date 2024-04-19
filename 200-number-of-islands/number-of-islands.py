class Solution(object):
    
    
    def numIslands(self, grid):
        m,n = len(grid),len(grid[0])
        visited=[[0 for i in range(n)] for j in range(m)]
        islands=0
        dir1=[0,1,0,-1]
        dir2=[1,0,-1,0]
        def bfs(x,y,m,n,grid,visited):
            
            
            q=[(x,y)]
            while(q):
                print(q)
                front = q.pop(0)
                x,y = front[0],front[1]
                for i in range(4):
                    new_x = x+dir1[i]
                    new_y = y+dir2[i]
                    if(0<=new_x<m and 0<=new_y<n and visited[new_x][new_y]==0 and grid[new_x][new_y]=="1"):
                        visited[new_x][new_y]=1
                        q.append((new_x,new_y))
        for i in range(m):
            for j in range(n):
                
                if visited[i][j]==0 and grid[i][j]=="1":
         
                    islands+=1
                    visited[i][j]=1
                    bfs(i,j,m,n,grid,visited)
        return islands
        
        
  
            
       
                        

                
                
            
                        
                        
                        
                
        