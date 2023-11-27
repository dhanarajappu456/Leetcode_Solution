#like the problem  - Maximize the Profit as the Salesman
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:


        
        pairs.sort(key = lambda x:(x[1],-x[0]))
        ans=  0
    
        prevEnd = -float("inf")

        for interval in pairs:

            if prevEnd<interval[0]:
                ans+=1
                prevEnd = interval[1]
            else:
                continue
        return ans


