class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
            
            s,e =0,len(nums)-1
            def binarySearch(firstOcc):
                targetInd = -1 
                s,e =0,len(nums)-1
                while(s<=e):
                    
                    mid =  s + (e-s)//2
                    if nums[mid]<target:
                        s = mid+1
                    elif nums[mid]>target:
                        e = mid-1
                    else:
                        
                        targetInd =   mid
                        if firstOcc:
                            e= mid-1
                        else:
                            s =  mid+1
                return targetInd
                
            
            return [binarySearch(True),binarySearch(False)]
            
                    
                    