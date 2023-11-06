class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        #as we traverse the array , check if prev element is lexicographically <=  or not

        charVal ={}
        for i,c in enumerate(order):
            charVal[c] = i

        def lexico(s1,s2):
            i,j  = 0 , 0 
            while(i<len(s1) and j<len(s2)):
               
                if charVal[s1[i]]<charVal[s2[j]]:
                    return True
                elif charVal[s1[i]]==charVal[s2[j]]:
                    i+=1
                    j+=1
                else:
                    return False
            
            return i==len(s1)

        n  = len(words)

        for i in range(1,n):
            
            if not lexico(words[i-1] ,words[i]):
                return False
        return True 
        