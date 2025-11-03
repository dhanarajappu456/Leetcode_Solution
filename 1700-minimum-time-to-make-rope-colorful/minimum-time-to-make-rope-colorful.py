class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        prev = 0 
        min_time = float("inf")
        time  = 0 
        n = len(colors)
        for i in range(1,n):
            if colors[i] != colors[prev]:
                prev  = i
            else:
                if neededTime[i] <= neededTime[prev] :
                
                    time += neededTime[i]
                else:
        
                    time += neededTime[prev]
                    prev = i 
        return time





        