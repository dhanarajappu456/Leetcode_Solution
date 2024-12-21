class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        m = len(wall)
        end  = sum(wall[0])
        cnt  = defaultdict(int)
        crossed = m
        for i in range(m):
            coord = 0 
        
            for j in range(len(wall[i])):
                wid = wall[i][j]
                coord+=wid
                if (coord != 0) and (coord!=end):
                    cnt[coord]+=1
                crossed =  min(crossed , m  - cnt[coord])

        return crossed
                