from collections import defaultdict as dict 


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        


        q= deque([(start_node,1)])

        ans  =[0 for i in range(n)]
        ans[start_node] = 1 

        adj = dict(list)
        m  = len(edges)
        for i in range(m):
            a,b  = edges[i][0],edges[i][1]
            adj[a].append((b,succProb[i]))
            adj[b].append((a,succProb[i]))

        while(q):


            node,node_prob =q.popleft()

            for neib,pr in adj[node]:
                if ans[neib]<pr*node_prob:
                    ans[neib] = max(ans[neib] , pr* node_prob)
                    q.append((neib,ans[neib]))

        return ans[end_node]