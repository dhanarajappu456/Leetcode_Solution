class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        s_map,g_map = defaultdict(int), defaultdict(int)
        cow,bull = 0,0
        for i,c in enumerate(secret):
            s_c = c 
            g_c =guess[i]
            if s_c != g_c:
                s_map[s_c]+=1
                g_map[g_c]+=1
            else:
                bull+=1
        for c in s_map:
            cow+= min(s_map[c],g_map[c])
        return str(bull)+"A"+str(cow)+"B"
            
        