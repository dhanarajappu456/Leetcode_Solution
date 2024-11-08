class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        
        mask=(1<<maximumBit)-1
        for i in range(len(nums)):
            mask^=nums[i]
            nums[i]=mask
        #result.reverse()
        return(nums[::-1])    
            
            
                    
        
                    
                    
                    