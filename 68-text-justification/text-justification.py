from collections import defaultdict as dict 

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        #create the map of lines mapped to the words list 

        map_  = dict(deque)
        last = -1
        line  = 0
        last_line =0 
        line_letters = [0 for i in range(400)]
        for i,w in enumerate(words):
            #if current word not fit in the line 
            #add it to the new line
            if (line_letters[line] +  len(map_[line])-1 + len(w) + 1)>maxWidth:
                line+=1 
            
            last_line  = line
            map_[line].append(w)
            line_letters[line]+=len(w)
        #generate the ans , using the map created above
        ans =[ ]
        for line in range(last_line+1):
          
            res = []
            width_remain =maxWidth
            words_remain  = len(map_[line])

            #for each word, we take the word , add the apces after that and repeat till all the word are placed for all ines
            for w in map_[line]:
                space = 0 
                #for last line , werds will have only 1 space b/w them 
                if line==last_line:
                    if words_remain!=1: 
                        space = 1
                
                #dividing the spaces evenly b/q the words for all the intermediate lines 
                else:
                    if words_remain>=2:
                        space = math.ceil((width_remain - line_letters[line])/(words_remain-1))
                res.append(w)
                res.append(" "*space)
                words_remain -=1
                width_remain-=(len(w)+space)
                line_letters[line]-=len(w)
         
          
            #this is to account for the last, line that , there may be spaces that might need to be appended at the end
            if width_remain >0:
                res.append(" "*width_remain)
                width_remain = 0
                    
            ans.append("".join(res))
       
        return  ans 



                


    