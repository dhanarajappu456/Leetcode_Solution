class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:

        nums.sort()
        ans = []
        i =0
        j=0
        n  = len(nums)
        while(i<n ):

            res =[]

            for j in range(i,i+3):
                if abs(nums[i]-nums[j])<=k: 
                    res.append(nums[j])
                
                else:
                    return []
            i=j+1
            ans.append(res)
        return ans 

                



        
        return ans
        