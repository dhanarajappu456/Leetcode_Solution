class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:

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
        #print(prevSmall , nextSmall)


        

        ans =  nums[k]

        for p ,  num in enumerate(nums):

            i = prevSmall[p]+1
            j = nextSmall[p]-1

            if i<=k<=j:
                #print(i,j, k ,num *(j-i+1))
                ans =max(ans, num *(j-i+1))
        return ans

        
