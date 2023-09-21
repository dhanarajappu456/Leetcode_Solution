class Solution:
    def minimumDifference(self, nums: List[int]) -> int:

        N = len(nums) // 2      
        ans = float("inf")
        total = sum(nums) 
        half = total // 2 
        ans= float("inf")
        for k in range(N+1):
            left = [sum(comb) for comb in combinations(nums[:N], k)]
            right = [sum(comb) for comb in combinations(nums[N:], N-k)]
        
            right.sort()
           
            for x in left:
                r = half - x
                p = bisect.bisect_left(right, r)
              
                #binary- se
                for q in [p-1,p]:
                        if 0<=q<len(right):
                       
                            leftSum,rightSum =  x+right[q] ,total -(x+right[q])
                            diff = abs(leftSum - rightSum)
                            ans = min(ans, diff) 
                        
        return ans