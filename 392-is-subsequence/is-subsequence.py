class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s=="":return True
        p1,p2=0,0
        
        while(p2<len(t)):
            
            if s[p1] == t[p2]:
                p1+=1
            if p1==len(s):
                return True
            p2+=1
        return  False 
    
    
    '''
    time  : o(st)
    space : o(1)
    
    
    
    followup 
    
    
    you can map the characters in t to their indices, 

    so that we dont need to iterate on the entire t when processing a string s 
    
    also  note  we will have to use binary search on  the list of indices of current processing character c  in s , to 
    get the index of c greater than previous index of t which was chosen 
    '''