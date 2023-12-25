

'''
#solution 1  not so efficient 
- you can use any basic graph traversal to update the prob of each node with max prob value 

here we use bfs

t -  v+ e  
s  v+e 


#solution 2 using djisktras algo - 

using maxheap , 
one thing to note is the prob is from <=1 

so when we traverse a path prob found so far remains same or is decreased along the path , 

there for for 2 edges emanating from a node, if one has more prob, then that is the first path that might give a better prob overall  so we 
greedily (maximum ) the graph in term of path probabiliy in case amidst travelling this path the tot prob reduced so much compared to other node in the maxheap , it is time to process the other nod 

thus making efficent algo that a node is processed just once approximately

t  elogv +  (v+e ) , djikstaras and adjlsit constr
a  (v+ e) adj list 

'''



# #solution 1
# from collections import defaultdict as dict 


# class Solution:
#     def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        


#         q= deque([(start_node,1)])

#         ans  =[0 for i in range(n)]
#         ans[start_node] = 1 

#         adj = dict(list)
#         m  = len(edges)
#         for i in range(m):
#             a,b  = edges[i][0],edges[i][1]
#             adj[a].append((b,succProb[i]))
#             adj[b].append((a,succProb[i]))

#         while(q):


#             node,node_prob =q.popleft()

#             for neib,pr in adj[node]:
#                 if ans[neib]<pr*node_prob:
#                     ans[neib] = max(ans[neib] , pr* node_prob)
#                     q.append((neib,ans[neib]))

#         return ans[end_node]


#solution 2
from collections import defaultdict as dict 
import heapq as h 
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
        maxHeap =  [(-1,start_node, )]
        while(maxHeap):


            node_prob,node =h.heappop(maxHeap)
            node_prob *=-1 

            for neib,pr in adj[node]:
                if ans[neib]<pr*node_prob:
                    ans[neib] =  pr* node_prob
                    h.heappush(maxHeap,(-ans[neib], neib))
                    

        return ans[end_node]