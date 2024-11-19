class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        j = 0
        n = len(nums)
        i = 0
        d = defaultdict(int)
        sum_ = 0 
        total_chars = 0
        ans = 0 
        while(j<n):
            d[nums[j]]+=1
            sum_+= nums[j]
            total_chars+=1
            if  (j-i+1 )<k :
                j+=1
                continue
            else:
               
                
                
                #if the count of unique chars is ==k 
                #then check if it could be an ans
                if len(d) ==k:
                     ans  = max(ans, sum_)
                #shrink the window
                sum_-= nums[i]
                d[nums[i]] -=1
                if d[nums[i]]==0:
                    d.pop(nums[i])
                i+=1
                j+=1
            
            
        return ans



            