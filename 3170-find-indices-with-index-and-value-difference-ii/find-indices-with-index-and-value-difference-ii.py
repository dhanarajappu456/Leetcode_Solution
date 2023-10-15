from collections import defaultdict as dict
from bisect import bisect
class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        
        org = nums.copy()
        n = len(nums)
        nums =[(num ,i) for i,num in enumerate(nums)]
        nums.sort()
       
        def first(num):
            ans = n
            l,h  = 0,n-1
            while(l<=h):
                
                m = (l+h)//2
                if nums[m][0]>=num:
                    ans = m
                   
                    h= m-1
                  
                else:
                    l= m+1
        
                   
            return(ans)
                        
        def last(num):
            ans = -1
            l,h = 0,n-1
            while(l<=h):
                
                m = (l+h)//2
                if nums[m][0]>num:
                    
                    h= m-1
                  
                else:
                    ans = m
                    l= m+1
            return(ans)
                        
        
        for i,num in enumerate( org):
            
            target1 ,target2  =  org[i] -valueDifference ,  org[i] + valueDifference
           
            a,b = last(target1),first(target2)
           
            
            # if a==-1:
            #     a= i
            # else:
            #     #fetch the actual index of the number in original array
            #     a = nums[a][1]
            # if b==-1:
            #     b=i
            # else:
            #   b=  nums[b][1]
            #print(i, a,b)
            
            while(a>=0):
                # if i==0:
                    
                #     print(a)
                if abs(nums[a][1]-i)>=indexDifference:
                    return [i,nums[a][1]]
                a-=1
            while(b<n):
             
                if abs(nums[b][1]-i)>=indexDifference:
                    return [i,nums[b][1]]
                b+=1
        return [-1,-1]
                
           
            
            
            
                       
                        
        

        #         last_occur = dict(int)

        #         for  i,num in enumerate(nums):

        #             last_occur[num] = i


        #         for i in range(n):
        #             target1 ,target2  =  nums[i] + valueDifference ,  nums[i] - valueDifference

        #             if target1  in last_occur and abs(last_occur[target1]-i)>=indexDifference:
        #                 return [i,last_occur[target1]]

        #             if target2  in last_occur and abs(last_occur[target2]-i)>=indexDifference:
        #                 return [i,last_occur[target2]]
        
#         def firstoccu
#         for i,num in enumerate(nums):
            
#             firstoccur(num-valueDifference)
#             lastocuur(num-valueDifference)



        
        return [-1, -1]
