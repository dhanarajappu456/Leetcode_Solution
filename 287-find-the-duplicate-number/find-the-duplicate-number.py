class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # 0th index will always be part of the cycle where the duplicate number fall
        s,f = 0, 0
        
        
        while(True):
            
            s = nums[s]
            f = nums[nums[f]]
            #like the problem - finding the start of the linked list  
            #when fast and slow meets , moving equidistant from this node and starting node , gives the star of cycle , 
            #which is the duplicate number
            
            if s==f:
                
                t1 ,t2 = 0,s
                while(t1!=t2):
                    t1 = nums[t1]
                    t2 = nums[t2]
                
                return t1
        