from collections import defaultdict as dict, deque  as deq

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        adj = dict(list)
        q = deq([])
        n = len(routes)
        for i in range(n):
            bus = i
            for j in range(len(routes[i])):
                stop = routes[i][j]
                adj[stop].append(bus)
        
        
        stopVis  =set()
        q.append((source, 0 ))
        stopVis.add(source)
        busVis = set()
        while(q):
            stop,busCount =q.popleft()
            if stop == target:
                return busCount
            for fromBus in adj[stop]:
                if fromBus not in busVis:
                    busVis.add(fromBus)
                    for neibStop in routes[fromBus]:

                        if neibStop not in stopVis:
                            q.append((neibStop,busCount+1))
                            stopVis.add(neibStop)
                            
        
        return -1


        