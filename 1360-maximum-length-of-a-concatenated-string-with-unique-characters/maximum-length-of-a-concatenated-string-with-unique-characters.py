class Solution:
    def maxLength(self, arr: List[str]) -> int:
        

        def is_unique(curr_word,prev_chosen):
            new_chosen  = prev_chosen[::]
            for c in curr_word:

                val = ord(c)-ord('a')
                if new_chosen[val]!=0:
                    return False
                new_chosen[val]+=1
          
            return new_chosen
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