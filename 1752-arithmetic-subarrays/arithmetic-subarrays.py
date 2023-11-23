class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:

        n  =len(nums)
        m = len(l)
        res  =[True for i in range(m)]
        for i in range(m):

            a,b =l[i],r[i]

            arr = nums[a:b+1]

            arr.sort()
            diff = arr[1]-arr[0]
            j=2
          
            while(j<len(arr)):
                if (arr[j]  - arr[j-1])!=diff:
                    res[i]=False
                    break
                j+=1
           
        return res
          