class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:


        '''
        note that the target is always sorted

        we keep pointer that point to current number target[p] in the target that need to be sufficed, 
        then we see if the current number(target[p]) is == that number we need to suffice from the target, if yes 
        then we can simply push to stack and increment the pointer, 
        else if the number in the stream is less than the target[p]  , then we need to simply push and pop the number 

        '''
        p =0 
        ans =[]
        for  i in range(1,n+1):
            if p ==len(target):
                return ans
            # if number in stream is< target[p] , then we dont need this number , 
            #so push and pop it 
            if i < target[p]:
                ans.extend(["Push","Pop"])
            #if nums[p] == the number in the strea, we need it, so push and keep it in stack
            else:
                ans.append("Push")
                p+=1
        
        return ans
        

        '''
        t :n 
        s :1 (excluding the ans array returned)
        '''