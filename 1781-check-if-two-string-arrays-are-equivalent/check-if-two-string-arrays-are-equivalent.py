'''
solution 1 

2 pass solution 
make the array to string - 1 traversal
then iterate th string to check equality

t mn  m,n = len of array and len of each word

s mn 



solution 2- one pass and no concatenation 

with 4 pointers
 
 2 pointers for each of the word list(a,b ) and 2 inner pointers for pointing current word in each of the wordlist(a1, b1)

 we iterate the inner pointers and if it reach end of curr word of word1 or word2 , then we need to make the outer pointer point to next word and inner pointer point to the starting letter of that new word

t mn 
s 1

'''

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        a,b  =0,0
        a1,b1 =0,0
        m,n  =len(word1), len(word2)
        while(True):

            
           
            #if current letter in the word not equal then return False
            if word1[a][a1] != word2[b][b1]:
                return False
            

           
            a1+=1
            b1+=1

            # if the current word is finished, move to next word in the list 
            # with the inner pointer pointing the start of the word
            if  a1==len(word1[a]):
                a1  =0 
                a+=1

            if b1 == len(word2[b]):
                
                b1= 0
                b+=1 
            
           
            #both pointer reached end of the list, then it is equal 
            if (a == m and b == n)  :
                return True
            
            #any one of it finished the wordlist , then it is not equal 
            if a==m: 
                return False
            elif b ==n : 
                return False
     

            


            
            
            
            

      