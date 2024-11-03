class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        

        def rec(node,prevColor):

            
            if color[node]!=-1:
                #take care of both parent and other nodes
                return prevColor!=color[node]

            color[node] = 1-prevColor
            
            for  neib in graph[node]:
                
                if rec(neib, color[node]) == False:
                    return False
            return True
        n = len(graph)
        color =[ -1 for i in range(n)]
        
        for i in range(n):
            if color[i]==-1:

                if rec(i,0) == False :
                    return False
        return  True
        



        