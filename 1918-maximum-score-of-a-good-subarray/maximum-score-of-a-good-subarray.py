class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        '''

            find the index of prevsmall and next small number  for each number 

            then iterate on the nums array , and each num as minimum of the  subarray and score  and also including k 
            find the score and store max score

        '''
        n = len(nums)
        prevSmall = [0 for i in range(n)]
        nextSmall = [0 for i in range(n)]
        stk =[(-1,-1)]
        for i ,num in enumerate(nums):
            while(stk and stk[-1][1]>= num):
                stk.pop(-1)
            
            prevSmall[i] = stk[-1][0]
            stk.append((i,num))
        stk =[(n,-1)]
        for i ,num in reversed( list(enumerate(nums))):
            while(stk and stk[-1][1]>= num):
                stk.pop(-1)
            
            nextSmall[i] = stk[-1][0]
            stk.append(( i,num))
        ans =  nums[k]
        for p ,  num in enumerate(nums):
            i = prevSmall[p]+1
            j = nextSmall[p]-1
            #if the subarray is good subarray , take the score into account
            if i<=k<=j:
                ans =max(ans, num *(j-i+1))
        return ans

        
