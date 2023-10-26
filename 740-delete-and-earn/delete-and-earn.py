from collections import defaultdict as dict 
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        #this keeps track of each elements count , which is needed to calculate the sum when  a number is chosen
        counts = Counter(nums)
        
        #we keep list of unique elements in the sorted order
        nums  = sorted(list(set(nums)))
       
        #this stores the max we can earn when choosing the prev number and not choocing the prev number
       
        prevChoice1 , prevChoice2 = 0,0
        n = len(nums)
        for i in range(n-1, -1,-1):
            '''currChoice1 is including the number
            curr choice 2 is max when not including the current number'''
            currChoice1 = nums[i]*counts[nums[i]]

            #a)case choosing the current number 
            # 1)if prev number visited is successsor of current, then , prev number cant be taken , 
            #hence the max sum when prev number  taken

          
            if i+1<n and nums[i+1]!=nums[i]+1:
                currChoice1 += max(prevChoice1, prevChoice2)
            #2) prev number is not successor
            else:
                currChoice1+= prevChoice2

            #b) case when current number is not chosen, then we can choose or not choose the prev number, hence the max w
            #when prev number is chosen and not chosen 
            currChoice2 =  max(prevChoice1,prevChoice2)
            prevChoice1,prevChoice2 = currChoice1, currChoice2
            
            
        return max(prevChoice1, prevChoice2)

        '''
        t n 
        s o(1) excuding the newly created nums list of unique element and the counter that keeps track of the count


        '''




        