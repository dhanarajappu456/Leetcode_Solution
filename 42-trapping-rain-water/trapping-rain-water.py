class Solution:
    def trap(self, height):
        
        
        n = len( height)
        l=0
        r =n-1 
        totalWater= 0
        maxLeftSofar,maxRightSoFar = 0,0
        while(l<=r):
            
            
            if height[l]<height[r]:
                trapedWater = max(0,min(maxLeftSofar,height[r])-height[l])
                maxLeftSofar= max(maxLeftSofar,height[l])
                l+=1
                
                
            else:
                trapedWater = max(0,min(maxRightSoFar,height[l])-height[r])
                maxRightSoFar= max(maxRightSoFar,height[r])
                r-=1
           
            totalWater += trapedWater
                
        return totalWater
                