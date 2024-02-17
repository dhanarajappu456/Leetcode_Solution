'''

solution 1 using 3d dp

ind,rembrick, remladd

make choices at each index

t n*b*l
s n*b*l


solution 2 using maxHeap

idea is to use the ladder as super power to jump very large heights
and use brick when making small jumps.



but we dont know which is larger jump, where we need to use the ladder 

so , idea is we start using brick at all possible situaion and , when we 
no more can use the rem brick for current jump we see in past we have used a max number of bricks
that >= current cost of jumping , in which case we use ladder in that past postion and 
collect those bricks to make current jump 

note: when checking if we have a max brick in past that can be used to jump current step

we are not taking   -maxheap[0]+ bricks >= cost

since this is not correct way doing

exmapl

1,9,19,21
b= 10
l=1

if we use this condtion then we might at max go till 2nd step 
but 3rd step is max we can can reach
t nlogb b = brick , n =len o f heights 
s b(brick)
'''


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
                
                    
                    
               