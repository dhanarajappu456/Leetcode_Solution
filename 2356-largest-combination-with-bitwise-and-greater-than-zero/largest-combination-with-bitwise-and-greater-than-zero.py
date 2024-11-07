class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        j = 1 
        ans = [ 0 for i in range(32)]
        for i in range(32):
            
            count = 0 
            for  num in candidates:
                if (num & j )!= 0:
                    count+=1
            ans[i] = count
            j<<=1 
        return max(ans) 
                
            

