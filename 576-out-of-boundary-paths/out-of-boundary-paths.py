'''

classic dp problem , where the i,j indicate the cell address and the rem denote the number of remaining moves

the state rec(i,j, rem) denote the number  ways we can move out from the cell i,j with rem number of
moves  left

t mn*maxMoves
s mn*MaxMoves + aux

'''


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dir =[(0,1),(1,0),(-1,0),(0,-1)]
        mod = 10**9+7
        @lru_cache(None)
        def rec(i,j,rem):

            if i==m or  j ==n or  i==-1 or j==-1:
                
                return 1
            ans = 0
            for d in dir:

                x,y = i+d[0],j+d[1]
                if rem > 0:

                    ans = (ans%mod + rec(x,y,rem-1)%mod)%mod

            return ans%mod

        return rec(startRow,startColumn,maxMove)


