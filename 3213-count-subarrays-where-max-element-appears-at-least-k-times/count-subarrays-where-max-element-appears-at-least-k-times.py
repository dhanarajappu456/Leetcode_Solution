
'''
essentially we find all the subarray with count of max element cnt_m>=k, ending at current index j 


sliding window

we go on extending the window till the count of max element in window<k 
once we reach the count ==k , we know we can form p number subarray ending at j where
p is different numbers at front such that count og max element in window ==k , 

to get this count we pop the chars at front(that is increment i) , till count of max element ==k 

when  this count<k,  now p is nothing but ==i(number  chars till index i-1)

this is repeated again , 

'




t n
 s 1

'''
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        m = max(nums)
        cnt_m = 0
        ans = 0 
        i=0
        j =0
        ans=0
        while(j<n):
            if nums[j] == m :
                cnt_m+=1
      
            while(cnt_m==k):
                if nums[i] == m:
                    cnt_m-=1
              
             
                i+=1      
            #all chars till index i-1  , can form differnt subarray satisfying the condition  
            ans += i
            j+=1

        return ans
    
        