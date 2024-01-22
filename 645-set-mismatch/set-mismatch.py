class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        set_=set()
        result=[]
        xor_=0
        miss,dup=0,0
        for i in nums:
            set_.add(i)
            
        for i in range(len(nums)):
            xor_^=(i+1)^nums[i]
            
        for i in range(1,len(nums)+1):
            if(i not in set_):
                miss=i
        dup=miss^xor_    
        return([dup,miss])
            