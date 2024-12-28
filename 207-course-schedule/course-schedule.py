from collections import defaultdict as dic


#make each course that can be succesfully completed to the dict as True,

# when the same course appear in ehe same path , then return False
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        topo=[]
        q=[]
        v= numCourses
        e = prerequisites
        indegree = [0 for i in range(v)]
        adj = dic(list)

        for i in range(len(prerequisites)):
            indegree[prerequisites[i][1]] += 1
            adj[prerequisites[i][0]].append(prerequisites[i][1])  
        
        for i in range(v):
            if indegree[i]==0:
                q.append(i)
   
        while q:
            front = q.pop(0)
            topo.append(front)
            for node in adj[front]:
                indegree[node]-=1
                if indegree[node]==0:
                    q.append(node)
      
        return len(topo)== v

            

        