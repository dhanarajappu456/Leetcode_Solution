class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:



        n = len(maxHeights)
        prevSmall = [(-1,0)]
        nextSmall = [(n,0)]
        leftSum  = [ 0 for i in range(n)]
        rightSum  = [0 for i in range(n)]
        #crate the monotonic stack from the front  - and populate the leftsum , denoting the max sum increading element to the left if maxHeights[i] is the peak


        for  i in range( n):

            while(prevSmall  and  prevSmall[-1][1]> maxHeights[i]):
                prevSmall.pop(-1)
            
            prevSmallInd =prevSmall[-1][0]
            prevSmallVal = prevSmall[-1][1]

            leftSum[i] =   ( leftSum[prevSmallInd]  if prevSmallInd!=-1 else 0) + prevSmallVal +  (i-prevSmallInd-1)*maxHeights[i]

            prevSmall.append((i,maxHeights[i]))
        
#crate the monotonic stack from the end   - and populate the rigth  , denoting the max sum of increasing element to the right  if maxHeights[i] is the peak
        for  j in range(n-1,-1,-1):

            while(nextSmall and nextSmall[-1][1]>  maxHeights[j] ):

                  nextSmall.pop(-1)
            
            nextSmallInd =nextSmall[-1][0]
            nextSmallVal = nextSmall[-1][1]

            rightSum[j] =   ( rightSum[nextSmallInd]  if nextSmallInd!=n  else 0) + nextSmallVal +  (nextSmallInd-j-1)*maxHeights[j]

            nextSmall.append((j,maxHeights[j]))

    
        ans =  0 
        for i in range(n):
            ans=  max (ans , maxHeights[i]  + leftSum[i] + rightSum[i])
        return ans 