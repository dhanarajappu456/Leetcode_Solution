class Solution:
    def minSwaps(self, nums: List[int]) -> int:
    

        i,j = 0,nums.count(1)-1
        cnt_one_wind = nums[i:j+1].count(1)
        tot_ones =nums.count(1)
        vis = 0 
        ans  = float("inf")
        n = len(nums)
        while(True):
            if i==0:
                vis+=1
            if vis ==2:
                break
            
            ans  = min(ans,tot_ones - cnt_one_wind)
            
            if nums[i]==1:
                cnt_one_wind-=1
            i = (i+1)%n
            
            j = (j+1)%n
            if nums[j] ==1:
                cnt_one_wind+=1
        
        return ans 
            



            
            


        
        


        

