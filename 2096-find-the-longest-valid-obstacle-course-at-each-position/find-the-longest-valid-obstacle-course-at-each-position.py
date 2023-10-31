import bisect

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        #approach1 - 
        
        #like the dp of lis , 

        #at each index, store the length of longest lis ending at i 
        # nums = obstacles 
        # n = len(nums)
        # dp =[1 for i in range(n)]
        # for i in range(n):
        #     j =i-1
        #     while(j>=0):
        #         if obstacles[j]<= obstacles[i]:
        #             dp[i]= max(dp[i], dp[j]+1)
        #         j-=1
        # return dp


        #approach2 - 
        
        #like the dp of lis , 

        #at each index, store the length of longest lis ending at i 
        #but we keep the longest increading subsequence in an array ,on which we run binary search 
        # to find the last occurence of the num(ans) in the lis array , so that num can be placed in ans+1
        #and the lis length is ans+2
        #to place the current number, that index, gives the lis for current num

        #this binary search  method is used to find length  of lis problem
    
        nums = obstacles 
        n = len(nums)
        lis  =[]
        dp =[1 for i in range(n)]


        def binSearch(lis,i):
            
            num = nums[i]
            ans  = -1
            s,e =0,len(lis)-1
            while(s<=e):
              
                m  = (s+e)//2
                if lis[m]<=num:
                  
                    ans = m 
                    s =m+1


                elif lis[m]>num:
                    e = m-1

            return ans+1
                
        for i,num  in enumerate(nums):  #n
            ind =binSearch(lis , i) #logn
            dp[i] = ind+1 
            if ind>=len(lis):
                lis.append(num)
            else:
               
                lis[ind] = num
            
          

            
        return dp


