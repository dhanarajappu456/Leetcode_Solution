

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        

        def bellman(i):

            d =[float("inf") for i  in range(n)]
            d[i] =0
            nodes = set()
            for _ in range(n-1):
                #relax edges in both direction, as is undir
                for a,b, w  in edges:

                    d[b] = min(d[b], d[a]+w)
                    d[a] = min(d[a], d[b]+w)
                 
            #dont consider the source node itself , when counting  the rechable node
            for v in range(n):
                if i!=v and d[v]<=distanceThreshold:
                    nodes.add(v)
            return nodes
            
            


        ans  = -1 
        min_cnt  = float("inf")
        for i in range(n):
            
            nodes  =  bellman(i)

            if len(nodes) <= min_cnt:
                min_cnt = len(nodes)
                ans = i


        return ans


            



        