from collections import defaultdict as dict 

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        mp = defaultdict(int)
        ans = 0 
        for num in answers:
            mp[num]+=1 
   
        '''

        the idea is for a  answer[i], let's call it num
        # for a num , max number of rabbits that has 
        #a specific color is num+1
        # so if you know count of rabbit with same color 
        # max that could fit in a particular color is count  / num+1
        # for rest it wuld be assigned a different color of same color 
        #but in a different group , let this number be chunks
        #this chunks is got by  math.ceil(count /( num +1) )
        #total rabbits = chunks * (num+1) , WHERE each chunks 
        #can max hold num+1 rabbits rabbits

        t n
        s n 
        ''' 
        for num in mp:
            count = mp[num]
            chunk  =   math.ceil(count /( num +1) )
            ans += chunk * (num+1)

        return  ans