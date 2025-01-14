class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        
        def check(i,j):
            pref,suff = 0, 0
            if len(words[i])<= len(words[j]):
                ln  = len(words[i])
                return words[j].startswith(words[i]) and words[j].endswith(words[i])
            return False                   
                    


        i=0
        n   = len(words)
        cnt =  0 
        while(i<n-1):
            j = i+1
            while(j<n):
                if check(i,j):
                    cnt+=1
                j+=1
            i+=1
        return cnt