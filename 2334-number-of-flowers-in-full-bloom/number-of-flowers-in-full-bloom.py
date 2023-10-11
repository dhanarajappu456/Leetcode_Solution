import heapq as h

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:

        '''

        for each person(sorted based on arrival ) keep  
        1)flower that bloomed  before  he arrived and  still in bloom and
        2)  all the flowers that started at the time he arrived. for this we need to have the flowers sorted by start time

        we push these flowers end time to the minHeap so that ,  for next person we might have to pop flowers which have stopped blooming


        '''

        flowers.sort()
        people_sorted  = sorted(people)
        ans ={}
        n= len(people)
        ptr = 0 
        minHeap = []
        for i in range(n): #p
            t = people_sorted[i]
            while(minHeap and minHeap[0]<t): #k*logf
                h.heappop(minHeap)
            while(ptr<len(flowers) and flowers[ptr][0]<= t): #klogf
                #skip all flowers that ended before this t
                if  flowers[ptr][1]< t:
                    ptr+=1 
                    continue
                #add all flowers which  bloomed before t or at t and still in bloom
                else:
                    st,end = flowers[ptr][0],flowers[ptr][1]
                    h.heappush(minHeap ,end )
                    ptr+=1
            ans[t] = len(minHeap)
        result =[0 for i in range(n)]
        for i in range(n):
            result[i] = ans[people[i]]
        return result

    '''

    t  =  p *k logf  = , p,f =people and flower, k is average size of heap at anu time 
    s  =  k , p = heap and ans dictionary size
    '''

           

    
           
        