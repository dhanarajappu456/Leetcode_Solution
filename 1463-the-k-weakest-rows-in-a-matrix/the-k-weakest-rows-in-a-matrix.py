class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        cnt =  [ (sum(m) , i) for i,m in enumerate(mat)]
        n = len(mat)
        cnt.sort()
        
        prev_val = -1
        
        ans = []
        i= 0
        while(i<k and prev_val<=cnt[i][0] ):
            ans.append(cnt[i][1])
            prev_val = cnt[i][0]
            i+=1
        return ans 