#solution 2 - using greedy 

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        m =Counter(nums)
        ans = 0 
        for num in m: 
            if m[num]==1:
                return -1
            else:
                ans += math.ceil(m[num]/3)
        return ans
       
    

            
        