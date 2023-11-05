class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
#         prevLarge = -1 
#         times = 0
#         deq =deque(arr)

#         while(True):
    
#             if deq[0]<deq[1]:
#                 index  = 0
#                 large = deq[1]
#             else:
                
#                 index = 1  
#                 large = deq[0]
            
#             if large != prevLarge:
#                 prevLarge =large
#                 times=0
#             times+=1

#             if times==k:
#                 return large

#             if index==0:

#                 val = deq.popleft()
#                 deq.append(val)
#             elif index ==1:
#                 val1,val2= deq.popleft(),deq.popleft()
#                 deq.appendleft(val1)
#                 deq.append(val2)



        n =len(arr)
        max_ = arr[0]
        max_ind = 0
        for i in range(1,n):
            
            if arr[i]>max_: 
                max_  = arr[i] 
                max_ind = i

            if max_ind ==0:
                if i - max_ind== k:
                    return max_       
            else: 
                if i - max_ind + 1  == k:
                    return max_
        return max_
           

        


        