'''

solution1 :
sorting and then comapring iadjacent to check if it occur once or twice

t nlogn 
s  1 



solution2 - using the count map

t n 
s n 


'''



#solution 2 
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:


        cnt  = defaultdict(int)
        ans1, ans2   = -1,-1
        for num in nums:
            cnt[num]+=1
        
        for num in cnt:
            if cnt[num] ==1 :
                if ans1 ==-1:
                    ans1=num
                else:
                    ans2  = num
        return [ans1, ans2]
            
        