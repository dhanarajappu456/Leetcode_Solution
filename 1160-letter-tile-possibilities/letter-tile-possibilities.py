class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        n =len(tiles)
        letters =  [ 0 for i in range(26)]
        res = set()
        for c in tiles:
    
            letters[ord(c)-65] +=1 
        cnt =0 
        def rec(s):
            nonlocal cnt 
            cnt+=1
            for j in range(26):

                if letters[j] == 0:
                    continue
                letters[j] -=1
                rec(s+ chr(j + 65) ) 
                letters[j] +=1
        
        rec("")
        return cnt-1

        