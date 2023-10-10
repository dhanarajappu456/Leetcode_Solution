class Solution:
    def minOperations(self, nums: List[int]) -> int:
    
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
     

     #t nlogn
     #s n (set)
        