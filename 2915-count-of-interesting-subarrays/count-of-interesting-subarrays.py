from collections import defaultdict as dict 
class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        

        remainder_cnt  = dict(int)
        n = len(nums)
        #create array indicating that , 1, 0 array ,where each element indicate, nums[i] % modul =k or not 
        valid_array = [ 1 if  nums[i]%modulo ==k else 0 for i in range(n)]
        print(valid_array)
        reminder_cnt = dict(int)
        remainder_cnt[0]+=1



        #at each index of valid_array,  go on  finding the prefix sum ,which indicate cnt of numbers upto i 
        #that , obeys nums[i]%modulo =k 
        #then  to get count of subarray ending at i ,with cnt%modulo = k , we check the map, where  we store , 
        #remainder -> number of times it is present at index 0 to i-1 
        ans=0 
        prefix_sum=0 
        for i in range(n):

            prefix_sum  += valid_array[i]
            rem = (prefix_sum % modulo )
            print(rem)
            ans +=remainder_cnt[(rem-k+modulo)%modulo]
            remainder_cnt[rem]+=1 
        return ans 

