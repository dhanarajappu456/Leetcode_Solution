class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        n  = len(words)
        def kmp(txt,pat):

            
            m1,m2  = len(txt), len(pat)
            lps = [0 for i in range(m2)]
            j = 0
            i =1 
            while(i<m2):
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

            while(i<m1):

                if pat[j] == txt[i]:
                    i+=1
                    j+=1
                
                else:
                    if j!=0:
                        j =  lps[j-1]
                    else:

                        i+=1
                if j == m2:
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

        