class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        color =[-1 for i in range(n)]
        for i in range(n):
            if color[i]==-1:
                    if self.dfs(i,graph,color,-1) == False:
                        return False
        return True
    def dfs(self,node,graph,color,parent):
        if parent == - 1:
            color[node]="B"
        else:
            color[node] = "G" if color[parent]=="B" else "B"
        for i in  graph[node]:
            if color[i] == -1:
                if self.dfs(i,graph,color,node) ==False:
                    return False
           
            if color[i]==color[node]:
                return False
        return True
                
