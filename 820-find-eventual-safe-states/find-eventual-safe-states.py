# from collections import defaultdict as dict

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        safe = dict()
        def dfs(node):
            

            if node in safe:
                return safe[node]

            safe[node] = False
            for neib in graph[node]:

                if dfs(neib)==False:
                    return False
                
            safe[node] = True
            return True

        n = len(graph)
        ans =[]
        for i in range(n):
            if dfs(i)==True:
                ans.append(i)
        return ans
        

        

                
