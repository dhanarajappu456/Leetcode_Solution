class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        mono_stk =[]
        n = len(nums)
     
        ans  = 0 
        for i,num in enumerate(nums):
         
            l,h = 0, len(mono_stk)-1
            left  = i
            while(l<=h):
               
                m = (l+h)//2
              
                if nums[mono_stk[m]]>num:
                    l=m+1
                else:
                    left = mono_stk[m]
                    h=m-1
            ans = max(ans,i-left)

    
            if mono_stk and nums[mono_stk[-1]]<num:
                continue
            mono_stk.append(i)
      
        return ans



        