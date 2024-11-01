import math as m
class NumArray:

    def __init__(self, nums: List[int]):

        
        self.numBins  =   m.ceil(len(nums)**0.5)
        self.binSize   =  m.ceil(len(nums)/self.numBins)
        #print(binSize, numBins)
        self.buckets=[0]*self.numBins
        self.nums = nums 
        for i in range(len(self.nums)):

            self.buckets[i//self.binSize]  += self.nums[i] 
        
        
    def update(self, index: int, val: int) -> None:

        diff = val - self.nums[index]
       
        self.buckets[index//self.binSize]+=diff
        self.nums[index] = val

        #print(self.buckets,self.nums)


    def sumRange(self, left: int, right: int) -> int:


        ans  = 0

        #`.summing the entire bucket all buckets sum 
        #from bucket1 to bucket2 
        #where bucket1 is bucket to which the element at
        #left falls to ,
        #bucket2 , is the bucket to which the element at 
        #right falls to 

        ans += sum(self.buckets[left//self.binSize:right//self.binSize])
        #2.  not that we can't  actually add the entire sum from buket2, 
        #as some of the element is not with in range left to right
        #cuz of which we included only elements that we needed
        ans+= sum(self.nums[(right//self.binSize)*self.binSize:right+1])
        #3. in step1. we considered all elements from the bucket1 
        # to the ans, so now we need to remove the unwanted elements
        #from the ans.
        ans-= sum(self.nums[(left//self.binSize )*self.binSize:left])
  

        return ans
