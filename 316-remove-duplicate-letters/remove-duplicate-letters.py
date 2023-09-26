class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        stk = []
        taken = {char:False for char in s}
        lastIndex = {c:i for i,c in enumerate(s)}
        print(lastIndex)
        for currCharInd , currChar in enumerate(s):
            #"abacb" -> expected  = "abc"
            while(stk and ( stk[-1]>currChar and taken[currChar]==False and  lastIndex[stk[-1]]>currCharInd) ) :

                curr = stk.pop(-1)
                taken[curr]= False
            if taken[currChar]==False:
                stk.append(currChar)
                taken[currChar] = True
        
        return "".join(stk)
            

