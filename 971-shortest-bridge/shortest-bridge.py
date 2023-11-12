from collections import deque as deq

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m, n  = len (grid), len(grid[0])
        def out(i,j):
            return i< 0 or j<0 or j>=n or i>=m
        q  = deq ([])
        vis  = set( )
        def dfs(i,j):
            
            if out(i,j) or (i,j) in vis or grid[i][j]==0:
                return 

            q.append((i,j,0))
            vis.add((i,j))
            dfs(i+1,  j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)


        firstIslandFound = False 
        for i in range(m):
            for j in range(n):
                
                if grid[i][j]==1:
                  
                    #collect all ones of a islands into a queue , with dfs
                    dfs(i,j)
                    firstIslandFound  = True
                    print("break")
                    break
            if firstIslandFound == True: 
                break
        
        while(q):
         
            i,j,dist = q.popleft()
            for d in [(0,-1),(-1,0),(0,1),(1,0)]:
                x,y  = i +d[0] , j+d[1]
                if not(out(x,y)) and (x,y) not in vis:
                    
                    if grid[x][y]==1:
                        return dist

                    q.append((x,y,dist+1))
                    vis.add((x,y))

        return 0


            


        