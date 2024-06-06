import heapq as h 
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        minHeap = []
        cnt = defaultdict(int)
        print(hand)
        curr_grp_size = 0
        for i,num in enumerate(hand):
            h.heappush(minHeap,num)
            cnt[num]+=1
        while(minHeap):

            while(minHeap and minHeap[0] not in cnt):
                h.heappop(minHeap)
            if minHeap:
                val = h.heappop(minHeap)
                rem =groupSize
                while(rem!=0):
                    if val in cnt:
                        rem-=1
                        cnt[val]-=1
                        if cnt[val]== 0:
                            cnt.pop(val)
                        val+=1
                    else:
                        return False
            else:
                return True
        return True




        
                
                
        
        
        
        
        