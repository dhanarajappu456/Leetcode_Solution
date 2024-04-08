'''
maxheap solution 
t nlogn n = len( stations)
s n 

to get shorter nuber of pumps, we need to jump max at each instatn, 
when we jump a dist max_reach , we store all unused pumps(infact, the fuel at that pump) from location 0 to max_reach , 
so that they can be used 
when needed. also note since these stored pump , must be such that it pump that can give pump with
 max fuel(so that max dist can be travelled), so we use maxheap
'''
import heapq as h

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        #max_reached so far
        max_reach = 0
        i =0 
        #store unused pump's fuel info
        max_heap = [-startFuel]
        ans = 0 
        while(max_heap):
    
            max_reach += -h.heappop(max_heap)
            
            if max_reach>=target:
                return ans
            
            #keep pushing the unused pumps tp maxheap
        
            while(i<len(stations) and stations[i][0]<=max_reach):
                h.heappush(max_heap,-stations[i][1])
                i+=1
            
            ans+=1
        return -1
            
            




