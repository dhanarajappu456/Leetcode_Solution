class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:

        pref ={-1:0}
        incr_stk = []
        ans = 0
        mod = 10**9+7

        for i,num in enumerate( nums):
            pref[i] =  pref[i-1]+num
        for i,num in enumerate(nums):
            newInd  = i
            while(incr_stk and num<incr_stk[-1][0]):
                val , ind = incr_stk.pop()
                l,r = ind-1, i-1
                ans  = max( ans, (val *  (pref[r]-pref[l])))
                newInd  = ind
            incr_stk.append((num, newInd))

        n =len(nums)
        for num,i in incr_stk:
            l,r  = i-1 ,  n-1
            ans  = max(ans,  (num*(pref[r]- pref[l])))
        return ans%mod



        







        