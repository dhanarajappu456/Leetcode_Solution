class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        n  = len(nums)
        sub_sums = [sum(nums[:k])]

        for i in range(1,n-k+1):
            sm = sub_sums[-1]+nums[i+k-1] -nums[i-1]
            sub_sums.append(sm)
   
        @lru_cache(None)
        def max_sm(i,cnt):

            if (cnt  ==0) or   (i ==n):
                return  0

            tk = 0
            not_ =0 
            if i<=n-k:
                tk = sub_sums[i]+ max_sm(i+k, cnt-1) 
                not_ = max_sm(i+1,cnt)

            return max(tk,not_)
        i=0 
        cnt= 3
        
        choosen =[]
       
        while((len(choosen)<3 ) and (i<=(n-k))):
            tk = sub_sums[i] + max_sm(i+k,cnt-1)
            not_ =  max_sm(i,cnt)
            '''
            remember we need to choose first i if 
            tk and not_tk gives a tie, 
            that is why we in case tk_ == not_ 
            also we append i
            '''
            if tk>=not_:
                choosen.append(i)
                i+=k
                cnt-=1
            else:
                i+=1
                
        return choosen

     