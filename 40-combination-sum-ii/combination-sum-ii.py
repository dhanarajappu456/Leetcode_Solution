class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        output = []
        n  = len(candidates )
        def rec(ind,res,sum_):
            
            if target == sum_:
                output.append(res)
                return 
            elif ind>=n or sum_> target:
                return 
            tk_ = rec(ind+1, res  +[ candidates[ind]], sum_ + candidates[ind] )

            while(ind+1<n and (candidates[ind+1] == candidates[ind])):
                ind+=1 

            not_ = rec(ind+1, res , sum_ )
           
            
        rec(0,[],0)
        return (output)