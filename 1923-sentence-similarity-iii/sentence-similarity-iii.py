class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        a1 , a2  = sentence1.split(" ") , sentence2.split(" ")
        i, j  = 0,0 
        m, n  = len(a1) , len(a2)

        k, l   = m-1 , n-1
        #matching the pref words in s1 and s2
        while(i<m and j<n and ( a1[i] == a2[j]) ):
            i+=1
            j+=1
        #matching the suff words
        while(k>=i and l>=j and ( a1[k] == a2[l]) ):
            k-=1
            l-=1
        #if there is subarray portion in both string taht can't be matched
        #in above steps, then it can't be made similar
        if i<=k and j<=l :
            return False
        #one can be made similar to another
        
        return True