class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        '''
            Input
            nums =
            [1,1,1,0,0,1,0,1,1,0]

            Use Testcase
            Stdout
            [3, 2, 1, 0, 0, 1, 0, 2, 1, 0]
            Output
            3
            Expected
            1
        '''
        n = len(nums)
        tot_one, tot_zero = 0,0
        # one = [ 0 for i in range(n)]
        # cnt = 0 
        # for i in range(n-1,-1,-1):
        #     if nums[i] ==0:
        #         cnt = 0 
        #         tot_zero+=1
        #         continue
        #     cnt+=1
        #     tot_one+=1
        #     one[i] = cnt
        # i= n-1
        # while(i>=0 and nums[i] ==1 ):
        #     i-=1
        
        # if i+1<n:
        #     #for edge case with just one element and is one ,ie  [1]
        #     if i+1!=0:
        #         one[i+1]+= one[0]
        # print(one)
        # ans  = float("inf")
        # for i in range(n):
        #     ans = min(ans, tot_one - one[i])
        # return  ans 

        if nums.count(1) ==1 :
            return 0
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
            



            
            


        
        


        

