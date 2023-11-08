#remeber u cant cache the result - 

# suppose adj lsit is 0->[1,2] , 1->[0]

# starting dfs , from 0 gives memo[0]= 3, memo[1] =1 , memo[1]

# again starting dfs on 1 should have been given 3, but , since 1 is cached u get 1 as the ans, which is wrong



'''

approach- if a bomb can detonate another then that bomb can detonate another ans do on , so it forma a connection 
so we form a dir graph, in which a node is adjacent to another , if it can detonate anotehr ,

'''
from collections import defaultdict as dict

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        

        adj = dict(list)

        n = len(bombs)
        for i in range(n):
            for j  in range(n):

                if i!=j:
                    x1,y1,r1 = bombs[i]
                    x2,y2,r2 = bombs[j]
                    #bomb[i] can dentonate bomb[j]  i then centerof bomb[j] mus lie within radius of bomb i , 
                    #that is dist b.w their center is <rad of bomb i 
                    if math.sqrt((x1-x2)**2 + (y1-y2)**2)<=r1:
                        adj[i].append(j)

        ans = 0
        def rec(node):
            if node in vis:
                return 0
            
            # not  count  redundant node that is visited as part of a starting node i 
            #eg: 0->1->2  0->2 , when we start dfs on 0 , it would visit 2 twice if we not use visited
            #also note to count back edge(child to parent)
            vis.add(node)
           
            nodes=0
            for neib in adj[node]:
                if neib not in vis:
                    nodes += rec(neib)
            return  1 + nodes
        #keeps all nodes visited for current node as the start node, and ensure each node counted only once
        vis =set()
        ans  = 1
        for i in range(n):
            #reset vis fot new node i as the start node, 
            vis = set()
            ans =max(ans, rec(i))
        return ans

        