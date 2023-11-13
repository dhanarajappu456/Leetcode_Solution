from collections import defaultdict as dict
'''




approach 1-

bruteforce
for  every query , run  from the query[i][0] and check if query[i][1] is present in any path
time : q*(v+e) for every query dfs takes (v+e)

space : adj list(v+e), stackspace ( v)   , v = n and e  = n^2 


approach 2 - efficient 

precompute the map "course" -> {set of other course, for which "course" is a prereq}
then answer the each query in O(1)



since there is no cycle, selfloop ,  it is simple for us  to cache the result 
run a dfs  from a node. visit all of its descndents,store it in memo[node.]

that is memo[node] store all the descndants of node, means it stores all the courses to which node is  prereq
once we have this cached result. 

we can detemine the each queries in o(1)


t  (v+e)+ q -> dfs takes o(v+e) = (n, n**2) , then processing queries takes queries length
s adj(n+n^2} + memo(n + n^2)+ stk(n)



'''

#approach2 
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        adj = dict(list)
        for s,e in prerequisites:
            adj[s].append(e)
        #maps a-> {b,c,d,e,...} ,where b,c,d,e.. are courses , for which a is a prereq
        memo = dict()

        def dfs(node):


            if node in memo:
                return memo[node]



            ans =  set()
            ans.add(node)

            for neib in adj[node]:

                ans = ans.union(dfs(neib))
            
            memo[node] = ans 
            return ans
        
        for i in range(numCourses):
            dfs(i)
        
        #print(memo)
        ans  =[]
        for s,e in queries:
            res = True if e in memo[s] else False 
            ans.append(res)
        return ans
            

         
        