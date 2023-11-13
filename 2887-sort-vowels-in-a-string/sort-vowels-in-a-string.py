class Solution:
    def sortVowels(self, s: str) -> str:
        lowerVowSet={'a','e','i','o','u'}
        upperVowSet = {"A","E","I","O","U"}
        lowerVowList =[]
        upperVowList =[]
        for c in s:
            if c in lowerVowSet:
                lowerVowList.append(c)
            elif c in upperVowSet:
                upperVowList.append(c)
        
        lowerVowList.sort()
        upperVowList.sort()
                
      
        res =[]
        l,u= 0,0 
        for i,c in enumerate(s):

            char =""
            if (c  not in lowerVowSet) and  (c not in upperVowSet):
                char  = c 
            else:
                if u<len(upperVowList):
                    char = upperVowList[u]
                    u+=1
                else:
                    char = lowerVowList[l]
                    l+=1
            res.append(char)
        return "".join(res)


        