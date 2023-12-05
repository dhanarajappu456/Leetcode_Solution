


'''
the algorithm is is simple. at any index we have 2 choice of take or not take the element 

we can determine if  the current word can be chosen or not using , an helper function ,
which checks if any lettr of the current word is chosen previously , with the help of list of length 26 , which 
indicate if the char is chosen so far or not 


t 2^n * n 

s  n 

'''

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        #helper for finding if the curr word can be chosen , provided the list of chars chosen so far
        #in case it can be chosen , return the new list of chars chosen , else return False
        def is_unique(curr_word,prev_chosen): #o(n)
            new_chosen  = prev_chosen[::]
            for c in curr_word:

                val = ord(c)-ord('a')
                if new_chosen[val]!=0:
                    return False
                new_chosen[val]+=1
          
            return new_chosen

        #The recursion , that aim to choose or not choose the current word
        n = len(arr)
        def rec(i,prev_chosen):
            if  i==n: 
                return 0
            new_chosen = is_unique(arr[i],prev_chosen)
            tk_,not_ = 0,0 
            if new_chosen:
                tk_ = rec(i+1,  new_chosen) + len(arr[i])
            not_ =rec(i+1, prev_chosen)
            return max(tk_,not_)
        return rec(0,[0 for i in range(26)])