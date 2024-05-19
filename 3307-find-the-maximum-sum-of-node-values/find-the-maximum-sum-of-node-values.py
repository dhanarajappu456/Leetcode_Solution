class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        
        count= 0
        min_xor_diff = float("inf")
        ans = 0 
        for num in nums:
            if num^k> num:
                count+=1 
                ans += (num^k)
            else:
                ans += num

            min_xor_diff = min(min_xor_diff,abs(num - ( num^k)))
            
        if count%2==1:
            return ans  - min_xor_diff
        return ans