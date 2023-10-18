from collections import defaultdict as dict

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        


        max_time = {}

        adj = dict(list)

        for course in relations:
            adj[course[0]].append(course[1])
        def rec(node):
            

            if node in max_time:
                return max_time[node]
            
            ans = 0
            for neib in adj[node]:
                ans  = max(ans,rec(neib))
            
            max_time[node] =  ans+time[node-1]
            return max_time[node]

        ans = 0 
        for node in range(1,n+1):
            ans = max(ans , rec(node))
        return ans

        