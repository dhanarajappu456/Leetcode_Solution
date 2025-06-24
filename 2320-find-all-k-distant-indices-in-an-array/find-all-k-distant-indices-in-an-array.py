class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n  = len(nums)
        first_index = [float("inf") for i in range(n)]
        ind  = float("inf")
        ans =  [ ]
        for i in range(n-1,-1,-1):
            if nums[i] == key:
                ind = i
    
            first_index[i] = ind
            
               
        print(first_index)
        for i in range(n):
            if nums[i] == key:
                ind = i
            if abs(first_index[i] - i) > abs(ind-i):
                first_index[i] = ind
        
        for i in range(n): 
            if abs ( first_index[i] - i)<=k:
                ans.append(i)
       
        
        return ans
        



        