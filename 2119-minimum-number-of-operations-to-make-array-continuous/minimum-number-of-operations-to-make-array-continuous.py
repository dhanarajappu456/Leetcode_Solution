class Solution:
    def minOperations(self, nums: List[int]) -> int:
        #binary search
        '''

        the same appproch as sliding window
        at each index we need to find largest continuous array , for finding the right end of the window 
        we use the binary search'''


        n =len(nums)
        ans  = n
        nums = sorted(set(nums))
    
        for l in range(len(nums)): #o(n)
     

            s,e = l+1,len(nums)-1
            ind =l
            target = nums[l] + n
            while(s<=e):
                m = (s+e)//2


                if nums[m] == target:
                    s = m
                    break
                elif  (nums[m]<target):
                   
                    s = m+1
                
                else:
                    e = m-1
            
       
            e = s
            s = l
       
            ans = min(ans,n - (e-l))
        return ans
     

     #t nlogn + nlgon sorting  and binary search
     #s n (set)
        