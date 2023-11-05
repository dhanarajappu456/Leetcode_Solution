class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        # prevLarge = -1 
        # times = 0
        # while(True):
    
        #     if arr[0]<arr[1]:
        #         index  = 0
        #         large = arr[1]
        #     else:
                
        #         index = 1  
        #         large = arr[0]
            
        #     if large != prevLarge:
        #         prevLarge =large
        #         times=0
        #     times+=1

        #     if times==k:
        #         return large


        #     val = arr.pop(index)
        #     arr.append(val)


        n =len(arr)
        max_ = arr[0]
        ind ={num: i for i,num in enumerate(arr)}
        for i in range(1,n):
            
            max_  =max(max_, arr[i])

            maxInd = ind[max_]
            #print(maxInd)
            if maxInd ==0:
                if i - maxInd== k:
                    return max_
                
            else: 
                if i - maxInd + 1  == k:
                    return max_
        return max_
           

        


        