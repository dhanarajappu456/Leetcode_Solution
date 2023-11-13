from collections import defaultdict as dict 
from sortedcontainers import SortedSet
#approach2 - suing counting sort

class Solution:
    def sortVowels(self, s: str) -> str:
        #this is traversed to give the next available character to be filled in current position of result
        sortedVowels= SortedSet("AEIOUaeiou")
        print(sortedVowels)
        ptr = 0
        #keeps track of avilable characters at any point of time in the string 
        vowCount =dict(int)
        res = []
        for c in s:
            if c in sortedVowels:
                vowCount[c]+=1
        
        for i,c in enumerate(s):

            char =""
            if c not in sortedVowels:
                char  = c 
            else:
                #to check which character in the sorted vowels is avilable 
                while( vowCount[sortedVowels[ptr]]==0):
                    ptr+=1
                vowCount[sortedVowels[ptr]]-=1
                char = sortedVowels[ptr]
            res.append(char)
        return "".join(res)


    '''

    t n(iterate on the string) 
    s 10 = map size, (lower and aupper vowels in worst)

    '''


