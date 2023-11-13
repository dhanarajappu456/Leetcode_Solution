from collections import defaultdict as dict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = dict(list)
        for s,e in prerequisites:
            adj[s].append(e)

        completed = dict()

        #run dfs, and return False if there is cycle, else  add the course to the resuklt in a post order fashion 
        ans   = []
        def dfs(node):

            if node in completed:
                return completed[node]

            completed[node]  = False
            for neib in adj[node]: 
                if dfs(neib)==False:
                    return False

            ans.append(node)
            completed[node] =True
            return True
        

        
        for i  in range(numCourses):
            if dfs(i) ==  False: 
                return []
        return ans 