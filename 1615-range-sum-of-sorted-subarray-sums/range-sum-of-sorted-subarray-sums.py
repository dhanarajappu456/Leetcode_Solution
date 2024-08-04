class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        mod  = 10**9+7 
        sm = [0 for i in range(max(nums)*n+1)]
        for i in range(n):
            s=0
            for j in range(i,n):
                s+= nums[j]
                sm[s]+=1
        i = 0 
        m = len(sm)
        ans = 0 
        #total terms to be summed
        needed  = right-left+1
        #skip these many terms , which comes before the index,  left
        # in the hypothetical sorted array 
        to_skip =left-1
        while(i<m and needed!=0):
            
            if sm[i]!=0:
                #rem stores the usable occurence of sum sm[i]
                rem  = sm[i]
                #we can use only those many occurence from cnt of terms with sum = sm[i],
                #after skipping "to_skip" terms and if at all anything remains
                if to_skip:
                    temp_rem = rem
                    rem = sm[i] - min(to_skip, rem)
                    to_skip  -=min(to_skip, temp_rem)
                #finding the ans
                ans = (ans%mod  + ( i*min(needed, rem)) %mod)%mod
                #now we need only these many terms to be summed
                needed -= min(needed, rem)
            i+=1
        return ans
                
                
             

                






        

        