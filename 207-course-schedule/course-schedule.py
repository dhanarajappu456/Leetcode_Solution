#cycle detection in dir grpah
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        ableToFinish = dict()
        adj = defaultdict(list)
        for s,e in prerequisites:
            adj[s].append(e)
        print(adj)

        def dfs(node):
            if node == 5:
                print(5555)


            if node in ableToFinish:
                if node == 5 : 
                    print(5, ableToFinish[node])
                return ableToFinish[node]
            
            ableToFinish[node] = False


            for neib in adj[node]:

                if dfs(neib) == False:
                    return False
            
            ableToFinish[node] = True
            return True 


        for i in range(numCourses):
            print(i)
            if dfs(i ) ==False:
                return False
        return True
        

        