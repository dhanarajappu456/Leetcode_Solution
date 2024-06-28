class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:


        deg = defaultdict( int )
        li = []
        val = n 
        ans = 0

        for a,b in roads:

            deg[a]+=1
            deg[b]+=1
     
        for node in deg:
            li.append(( node, deg[node]) )
        li.sort(key = lambda x:-x[1])

        for node,d in li:
            ans += val*d
            val-=1
        return ans 