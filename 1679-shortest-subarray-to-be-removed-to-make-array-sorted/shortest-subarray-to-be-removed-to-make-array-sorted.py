class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        ans = n
        i,j = 0 , n-1
        while(j>0 and   arr[j]>=arr[j-1]):
            j-=1

        #in case 15, 10,1,2,3,4,5,6 
        #front portion might need ro be removed which is == j 
      
        ans  = min(ans, j)

        #there will be portion that need to be removed will be in between
        #1,2,8,[2,4],30,40,50,60 - > ans =2, remove [2,4]
        #10,20,30,32,38,40,[54,60],43,44,48,49,50 ans 2 , remove[54,60]
        
        # incrementing i , if nums[i] <= nums[j]
        # else , we may try incrementing j, till nums[j]< nums[i]
        
        while(i<j and (i==0 or arr[i]>= arr[i-1])) :
            while(j<n and arr[i]>arr[j]):
                j+=1
            ans  = min(ans , j-i-1)
            i+=1

        return ans 