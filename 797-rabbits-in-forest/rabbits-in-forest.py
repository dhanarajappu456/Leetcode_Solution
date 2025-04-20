from collections import defaultdict as dict 

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        mp = defaultdict(int)
        ans = 0 
        for num in answers:
            mp[num]+=1 
   

        for num in mp:
            count = mp[num]
            chunk  =   math.ceil(count /( num +1) )
            ans += chunk * (num+1)

        return  ans