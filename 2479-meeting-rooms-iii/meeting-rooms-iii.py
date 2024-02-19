import heapq as h 

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms =[0 for i in range(n)]
        available  =[i for i in range(n)]
        h.heapify(available)
        meetings.sort(key = lambda x: (x[0],x[1]))
        #print(meetings)
        curr_meeting = []
        for m in meetings:
            
            while curr_meeting and curr_meeting[0][0]<=m[0]:
                end , ind  = h.heappop(curr_meeting)
                h.heappush(available,ind)
            if len(available) ==0 :
                end, ind  = h.heappop(curr_meeting)
                new_end  = max(m[0],end)+m[1]-m[0]
                h.heappush(curr_meeting,(new_end,ind))
                rooms[ind]+=1
            else:
                # while(curr_meeting and curr_meeting[0][0]<=m[0]):
                #     end, ind = h.heappop(curr_meeting)
                #     available.add(ind)
                    ind = h.heappop(available)
                    end = m[1]
                    h.heappush(curr_meeting,(end,ind))
                    rooms[ind]+=1
            #print(curr_meeting)
        #print(rooms)
        max_ind = None
        count= 0
        for ind,cnt  in enumerate(rooms) :
            if cnt>count:
                max_ind = ind
                count =cnt
        return max_ind

            