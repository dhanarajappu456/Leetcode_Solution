class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        ans  = float("inf")
        n =  len(nums)
        ors = 0 
        i  = 0
        j= 0 
        bits=[0 for i in range(32)]

        def remove(bits,num):
            for i in range(32):
                if (num&(1<<i))!=0 :
                    bits[i]-=1
             
                    
        def add(bits,num):
            for i in range(32):
                if (num&(1<<i))!=0 :
                    bits[i]+=1
            
        def get_decimal(bits):
            ans =  0 
            for i in range(32):
                if bits[i] >=1:
                    ans|=(1<<i)
            return ans
        while(j<n ):
            add(bits,nums[j])
            if get_decimal(bits)<k:
                j+=1
                continue
            while(i<=j and get_decimal(bits)>=k):
           
                ans = min(ans,j-i+1)
                remove(bits,nums[i])
                i+=1
            j+=1
        return -1 if ans == float("inf") else ans