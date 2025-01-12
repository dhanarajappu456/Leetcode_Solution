class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        n  = len(words)
        def kmp(txt,pat):

            
            m,n  = len(pat),len(txt)
            lps = [0 for i in range(m)]
            j = 0
            i =1 
            while(i<m):
                if pat[i] == pat[j]:
                    lps[i] = j+1
                    i+=1
                    j+=1
                else:
                    if j>0:
                        j = lps[j-1]
                    else:
                        i+=1
          
            j =0
            i= 0

            while(i<n):

                if pat[j] == txt[i]:
                    i+=1
                    j+=1
                
                else:
                    if j!=0:
                        j =  lps[j-1]
                    else:

                        i+=1
                if j == m:
                    return True
            return False
                


                



        ans  = []
        for i in range(n):
            match_ = 1
            for j in range(n):

                if j!=i:
                    if kmp(words[j], words[i]):
                        ans.append(words[i])
                        break
        return ans

        