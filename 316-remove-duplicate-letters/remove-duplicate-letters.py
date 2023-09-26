class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        '''

        the idea is whene all the  characters are alwats increasing , then that string itself, is the  smallest lexicographical order


        but any index if a character is < previous character, then we might remove all the previous character, 
        which are lesser than the current char iff:
        a)the current character is new character that is not present in the previously chosen set of character (taken is used for this)
        and
        b)the previous character comes again after this current character(that is why , last index store the last occurence of each distinct characater )

        obeying these condition , we can remove the previous character
        '''
        stk = []
        #to know if current character  is not present in the set of chosen previous chars, thereny making sure that the 
        #it is new character, that can  be chosen 

        taken = {char:False for char in s}
        #to determine if the stk top character  ,  appears again after the curr character index, so that top char, can be removed safely 
        lastIndex = {c:i for i,c in enumerate(s)}
    
        for currCharInd , currChar in enumerate(s):
            #the condition so that the previously chosen character , can be deleted 
            #"abacb" -> expected  = "abc"
            while(stk and ( stk[-1]>currChar and taken[currChar]==False and  lastIndex[stk[-1]]>currCharInd) ) :

                curr = stk.pop(-1)
                taken[curr]= False
            if taken[currChar]==False:
                stk.append(currChar)
                taken[currChar] = True
        
        return "".join(stk)
            

