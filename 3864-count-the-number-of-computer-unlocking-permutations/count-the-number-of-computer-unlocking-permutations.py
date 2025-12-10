class Solution:
    def countPermutations(self, complexity: List[int]) -> int:



        #if there is a lock , that has comp less than the root ,then 
        #we can't unlock the locks
        mod  = 10**9 +7
        mn  = min(complexity)
        if (mn < complexity[0] ) or (complexity.count(mn)>1 and complexity[0] ==  mn):
            return 0 
        n = len(complexity)

        return math.factorial(n-1)%mod

        