from collections import defaultdict as dict

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        grp  = dict(set)

        for member, size in enumerate(groupSizes):

            grp[size].add(member)
        
        res =[]
        ans =[ ]
        for size in grp:
            for memb in grp[size]:
                res.append(memb)
                if len(res)==size:
                    ans.append(res.copy()) 
                    res  =[]
               
                   
        return ans
