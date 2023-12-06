'''
#solution 1

greedy solution 

store count of each char in freq map 

now for each char in the map if the frequency  is already used find  the very next lowest frequency that can be possibile for 
this character, so that remaining chars can be deleted 

t = creating map(n) + we might have at max 26 freq so the total unmber of time loop runs is const almmost

s freq map + set = o(26)


'''
from collections import defaultdict as dict

class Solution:
    def minDeletions(self, s: str) -> int:
        

        freq =dict(int)
        freq_Used= set()
        for c in s :
            freq[c]+=1
        ans = 0
       
        for  c in freq:#at max can have 26 type of freq
            frequency = freq[c]
            while(frequency in freq_Used):
                frequency-=1
            ans += freq[c] - frequency
            if frequency!=0:
                freq_Used.add(frequency)
        return ans
