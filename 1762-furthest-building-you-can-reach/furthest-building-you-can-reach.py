import heapq as h

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        maxHeap =[]
        n =len(heights)
        for i in range(n-1):
            cost = heights[i+1] - heights[i]
            if cost>0:

                if cost<=bricks:
                    bricks-=cost
                    h.heappush(maxHeap,-cost)
                elif ladders>0:

        
                    if maxHeap and -maxHeap[0]>=cost:
                        max_brick = -h.heappop(maxHeap)
                        bricks +=  max_brick - cost
                        h.heappush(maxHeap,-cost)

                    ladders-=1
                
                else:
                    return i
        return n-1
                
                    
                    
               