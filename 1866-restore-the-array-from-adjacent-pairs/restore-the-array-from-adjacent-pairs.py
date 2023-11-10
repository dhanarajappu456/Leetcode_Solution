from collections import defaultdict as dict 
'''

we create a map  -> number :neib1, neib2

where neib 1 and 2 are neibrs on either side of the number

after creating  this it is all about finding  either start or end of the sequence(which is that number which has only 1 neighbour), then start creating the sequence , with the help of the map ,

also we add the already added numbers into the sequence , to a visited set

'''
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:

        vis = {}
        adj = dict(list)

        n = len(adjacentPairs)+1
        #creating the neib list
        for p in adjacentPairs:

            a,b = p[0],p[1]

            adj[a].append(b)
            adj[b].append(a)

        start = None
        for i in adj: 
            if len(adj[i])==1:
                start = i
                break 
        ans = []
        vis  = set()
        while(len(ans)!=n):
            ans.append(start)
            vis.add(start)

            for adjacent in adj[start]:
                #choose that neib of the number, which is not already added to the sequence
                if adjacent not in vis:
                    start = adjacent
 
        return ans 


        