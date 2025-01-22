class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[ 0])
        q = deque([])
        ans = [ [ 0 for j in range(n)] for i in range(m)]
        vis  = set()
        for i in range(m):
            for j in range(n):
                if isWater[i][j] ==1:
                    ans [i][j] = 0 
                    q.append((i,j,0))
                    vis.add((i,j))
        dir_ = [(0,1),(1,0),(-1,0),(0,-1)]
        
        while(q):
            i,j,frontier  = q.popleft()
            for d in dir_:
                x,y = i+d[0],j+d[1]
                if (0<=x<m) and (0<=y<n) and ((x,y)  not in vis):
                    vis.add((x,y))
                    ans[x][y] = frontier+1
                    q.append((x,y,frontier+1))
        return ans
        
        