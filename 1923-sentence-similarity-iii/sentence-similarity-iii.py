class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        a1 , a2  = sentence1.split(" ") , sentence2.split(" ")
        i, j  = 0,0 
        m, n  = len(a1) , len(a2)

        k, l   = m-1 , n-1
        while(i<m and j<n and ( a1[i] == a2[j]) ):
            i+=1
            j+=1
        
        while(k>=i and l>=j and ( a1[k] == a2[l]) ):
            k-=1
            l-=1
        
        if i<=k and j<=l :
            return False

        return True