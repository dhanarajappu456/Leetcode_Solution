class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        #keeps the pref sum ending at all index, 
        pref ={-1:0}
        #mono increasing stack 
        incr_stk = []
        ans = 0
        mod = 10**9+7
        #calculater the pref sum 
        for i,num in enumerate( nums):
            pref[i] =  pref[i-1]+num
        
        for i,num in enumerate(nums):
            newInd  = i
            while(incr_stk and num<incr_stk[-1][0]):
                val , ind = incr_stk.pop()
                l,r = ind-1, i-1
                #the popped elements form the min max - product subarray  , wheer right end is the i-1
                ans  = max( ans, (val *  (pref[r]-pref[l])))
                #the current element is put at index, newind , which is last 
                #index, of laset popped element , as current num can form the min max subarray ,  ,
                # with all of the popped element
                newInd  = ind
            incr_stk.append((num, newInd))

        #at the end stack will have the increasing subarray , so find the subarray sum again 
        n =len(nums)
        for num,i in incr_stk:
            l,r  = i-1 ,  n-1
            ans  = max(ans,  (num*(pref[r]- pref[l])))
        return ans%mod



        







        