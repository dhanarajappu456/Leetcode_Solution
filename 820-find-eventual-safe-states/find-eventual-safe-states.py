# from collections import defaultdict as dict

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        safe = dict()
        def dfs(node):
            
            #base case - if cycle or already processed node, then return value False and True 
            if node in safe:
                return safe[node]
            #intially until all the path is known to lead to tail node, mark it as unsafe 
            safe[node] = False
            for neib in graph[node]:
                
                if dfs(neib)==False:
                    return False
                
            safe[node] = True
            #now the node is known to be safe, so true , is stored,
            return True

        n = len(graph)
        ans =[]
        for i in range(n):
            if dfs(i)==True:
                ans.append(i)
        return ans
        

        

                
