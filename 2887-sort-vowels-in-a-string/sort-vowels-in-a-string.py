class Solution:
    def sortVowels(self, s: str) -> str:
        vowelSet={'a','e','i','o','u', "A","E","I","O","U"}
        vowList =[]
 
        for c in s:
            if c in vowelSet:
                vowList.append(c)
      
        
        vowList.sort()

     
                
      
        res =[]
        v = 0 
        for i,c in enumerate(s):

            char =""
            if c not in vowelSet:
                char  = c 
            else:
                char = vowList[v]
                v+=1
            res.append(char)
        return "".join(res)


    '''

    t n(iterate on the string)  + klogk ,  k= len(vowelist, at worst  it can be n )
    s k(at worst can be n )

    '''


