class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row, col = defaultdict(int), defaultdict(int)
        m,n = len(grid) , len(grid[0])
        #check for the row 
        #check for rhe cols

        for i in range(m):
            r = 0 
            for j in range(n):
                if grid[i][j] ==1:
                    r+=1
            row[i] = r
        for j in range(n):
            c = 0 
            for i in range(m):
                if grid[i][j] ==1:
                    c+=1
            col[j] = c
        print(row, col)
        ans = 0 
        for i in range(m):
            for j in range(n):
                if grid[i][j] ==1 :
                    if row[i] > 1 or col[j]>1:
                        ans+=1
        return ans




                