class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        output = []
        def rec(ind,res,sum_):
            
            if target == sum_:
                output.append(res)
                return 
            
            for i in range(ind,len(candidates)):
                
                if i>ind and candidates[i-1] == candidates[i]:
                    continue
                if sum_ + candidates[i] >target :
                    break
                rec(i+1,res+[candidates[i]],sum_ + candidates[i])
                
            
        rec(0,[],0)
        return (output)