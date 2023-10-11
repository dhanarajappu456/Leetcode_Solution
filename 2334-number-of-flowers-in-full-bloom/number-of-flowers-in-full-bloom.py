import heapq as h

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:

       

        flowers.sort()
        people_sorted  = sorted(people)
        print(flowers)
        ans ={}
        n= len(people)
        ptr = 0 
        minHeap = []
        
        for i in range(n):
            t = people_sorted[i]
           
            while(minHeap and minHeap[0]<t):
                h.heappop(minHeap)
            #print(t, minHeap,minHeap[-1] if minHeap else 0 )
            while(ptr<len(flowers) and flowers[ptr][0]<= t):

                #skip all flowers that ended before this t
                if  flowers[ptr][1]< t:
                    ptr+=1 
                    continue
                #add all flowers which  bloomed before t or at t and still in bloom
                else:
                    st,end = flowers[ptr][0],flowers[ptr][1]
                    h.heappush(minHeap ,end )
                    ptr+=1
            #print(minHeap)
            ans[t] = len(minHeap)
        result =[0 for i in range(n)]
        for i in range(n):
            result[i] = ans[people[i]]
        return result


           

    
           
        