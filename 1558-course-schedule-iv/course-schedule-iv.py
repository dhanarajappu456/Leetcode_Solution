from collections import defaultdict as dict

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        adj = dict(list)
        for s,e in prerequisites:
            adj[s].append(e)
        #maps a-> {b,c,d,e,...} ,where b,c,d,e.. are courses , for which a is a prereq
        memo = dict()

        def dfs(node):


            if node in memo:
                return memo[node]



            ans =  set()
            ans.add(node)

            for neib in adj[node]:

                ans = ans.union(dfs(neib))
            
            memo[node] = ans 
            return ans
        
        for i in range(numCourses):
            dfs(i)
        
        #print(memo)
        ans  =[]
        for s,e in queries:
            res = True if e in memo[s] else False 
            ans.append(res)
        return ans
            

         
        