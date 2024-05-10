'''
using heap - min 
first the smallest number would be arr[0]/arr[n-1]
second smallest number could be one either arr[0][n-2] 
or arr[1][n-1], so now you got the , something like a two pointer, 
so we will put all the possible answer heap and pop k-1 smallest fraction 
whilepopping , we need to make sure that  next possible ans could be fraction made of number at i,j (and is to be pushed to heap)
where i the  the index of numerator in the fraction  popped 
and j is the index of number to left of number in denominator of fraction popped

t nlong  + klogn
s

'''

import heapq as h 

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        min_heap = []
        h.heapify(min_heap)
        n =len(arr)
        #push all the smallest freaction possible with all possible numbers as the 
        #(ie, keeping the denominator as the largest  num in the number , and numerator as all possible nums 
        #in the array )
        #nlogn
        for i in range(n-1):
            h.heappush(min_heap,(arr[i]/arr[n-1],i,n-1))
        #klogn
        while(k>1):
            fr,i,j = h.heappop(min_heap)
            #pushing the next possible ans to the heap
            h.heappush(min_heap , (arr[i]/arr[j-1],i,j-1))
          
            k-=1
        #at end fraction at top is ans
        v1,v2 = arr[min_heap[0][1]],arr[min_heap[0][2]]
        return [v1,v2]        


            
      
