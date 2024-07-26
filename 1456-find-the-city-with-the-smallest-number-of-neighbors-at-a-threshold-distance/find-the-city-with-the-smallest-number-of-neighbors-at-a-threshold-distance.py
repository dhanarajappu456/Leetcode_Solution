

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

       
        #v^3
        def floyd():

            d = [[ 0 if i == j else float("inf")  for i in range(n)] for j in range(n)]
            for a,b ,w in edges:

                d[a][b] = w
                d[b][a] = w 
            #for all the pair of nodes(j,k), find the shortest path through node i 
            for i in range(n):

                for j  in range(n):

                    for  k in range(n):

                        d[j][k] = min(d[j][k], d[j][i] + d[i][k])

            ans  = -1 
            min_cnt  = float("inf")
            for i in range(n):
                nodes = set()
                for j in range(n):
                    #dont consider source node 
                    if  i!=j and d[i][j] <= distanceThreshold:
                        nodes.add(j)

                if len(nodes) <= min_cnt:
                    min_cnt = len(nodes)
                    ans = i

            return ans 

        return floyd()
