from collections import defaultdict as dict 

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        cnts = defaultdict(int)
        n  = len(A)
        ans = 0 
        res =[ ]
        for i in range(n): 
            c = A[i]
            cnts[c]+=1
            if cnts[c] == 2:
                ans+=1
            c = B[i]
            cnts[c]+=1
            if cnts[c] == 2:
                ans+=1
            res.append(ans) 
        return res
                



