from collections import defaultdict as dict 

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:

        l1 =s1.split(" ")
        l2  = s2.split(" ")
        ans = []
        m1, m2 =dict(int), dict(int)
        for w in l1:
            m1[w]+=1
         
        
        for w in l2:
            m2[w]+=1

        

        for w in m1:
            if m1[w]==1 and w not in m2:
                ans.append(w)
        
        for w in m2:
            if m2[w]==1 and w not in m1:
                ans.append(w)
        return ans