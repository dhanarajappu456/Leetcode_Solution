from collections import defaultdict as dict 
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:

        mp_even_ind  = [0 for i in range(26)]
        mp_odd_ind = [0 for i in range(26)]

        for i in range(len(s1)):
            if i%2 ==0:
                
                mp_even_ind[ord(s1[i])-97]+=1
                mp_even_ind[ord(s2[i]) -97]-=1
             
            else:
                mp_odd_ind[ord(s1[i])-97]+=1
                mp_odd_ind[ord(s2[i]) -97]-=1
        print(mp_even_ind, mp_odd_ind)
        return all(num==0 for num in mp_even_ind ) and all(num==0 for num in mp_odd_ind )


        