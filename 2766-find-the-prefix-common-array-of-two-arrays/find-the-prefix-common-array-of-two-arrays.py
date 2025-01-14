from collections import defaultdict as dict 

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        d_a = dict(int)
        n = len(B)
        res = [ 0 for i in range(n)]
        for i in range(n):
            d_a[A[i]]+=1
            used = dict(int)
            ans =0 
            for j in range(i+1):
                if d_a[B[j]]>0:
                    ans +=1
                    used[B[j]]+=1
                    d_a[B[j]]-=1
            res[i] = ans 
            for val in used:
                d_a[val]+= used[val]
        return res
                



