class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans  =[]
        n = len(nums)
        def rec(i,sub):
            
            if i  == n :
                ans.append(sub)
                return 
            
            rec(i+1,sub+[nums[i]])
            rec(i+1,sub)
        rec(0,[])
        return ans

        