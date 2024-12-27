class Solution:
    def findMin(self, nums: List[int]) -> int:


        ans  = float("inf")
        n = len(nums)
        s,e  = 0, n-1
        while(s<=e):
            m = (s+e)//2 


            ans  = min(nums[m],ans)

            #avoid duplicate condition
            '''
            [10,1,10,10,10]
            ''' 
            if (nums[s] == nums[m]) and (nums[m] == nums[e]):
                s+=1
                e-=1
                continue

            
            #[3,4,5,1,2], that is why we store the min in to ans beforehand , on above line 
            if nums[s]<=nums[e]:
                ans = min(ans,nums[s])
          
            
            if nums[s]<=nums[m]:
                #this line is not needed
                #ans = min(ans,nums[s])
                s = m+1
           
            elif nums[s]>nums[m]:
                #edge case : what if the  mid itself is the minimum , that is why we store the min to ans before moving
                #[3,4,1,2,3]
                ans = min(ans,nums[m])
                e = m-1

        return ans 
       