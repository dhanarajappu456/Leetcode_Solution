'''
#solution 1

greedy solution 

store count of each char in freq map 

now for each char in the map if the frequency  is already used find  the very next lowest frequency that can be possibile for 
this character, so that remaining chars can be deleted 

t suppose we need to iterate till 0 inside the while , so tha all freq is taken 
then character may have 1,2,3,4,... count so  on 

then the number unque freq can be applying sum formula o(n^2) = 10^5
then n approx  =1000
so we might have 1000 type of unique freq continuously , and then we might run on them for  freq of current characte in the map 
so t  = 1000^2 = 10^6

s freq = o(sqrt(n))  = o(1000)


'''
from collections import defaultdict as dict

class Solution:
    def minDeletions(self, s: str) -> int:
        

        freq =dict(int)
        freq_Used= set()
        for c in s :
            freq[c]+=1
        ans = 0
       
        for  c in freq:
            frequency = freq[c]
            while(frequency in freq_Used):
                frequency-=1
            ans += freq[c] - frequency
            if frequency!=0:
                freq_Used.add(frequency)
        return ans
