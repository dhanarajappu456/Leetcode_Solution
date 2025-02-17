class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        n =len(tiles)
        used =  [False for i in range(n)]
        res = set()
        
        def rec(s):
            res.add(s)
            for  j in range(n):

                if  used[j]:
                    continue
                used[j] = True
                rec(s+tiles[j] ) 
                used[j] = False
        
        rec("")
        return len(res)-1 

        