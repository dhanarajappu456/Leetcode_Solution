class Solution:
    def trap(self, height: List[int]) -> int:
        heights = height 
        n = len(heights)
        l,r = 0,n-1
        lMax,rMax = 0,0
        ans= 0
        while(l<=r):
            
            if heights[l]<heights[r]:
                currentHeight = heights[l]
                limitingHeight  = lMax
                if limitingHeight >=currentHeight :
                    ans+=(limitingHeight - currentHeight)
                lMax=  max(lMax,heights[l])
                l+=1
                
            else:
                currentHeight = heights[r]
                limitingHeight  = rMax
                if limitingHeight >= currentHeight:
                    ans+=(limitingHeight -  currentHeight)
                rMax=  max(rMax,heights[r])
                r-=1
                
        return ans