class Solution:
    # the idea is the answer is  "a" + p shifts
    #where p is the number of set bits in k-1, which is hte index value at which we 
    #need to find the character
    def kthCharacter(self, k: int) -> str:
        index = k-1
        set_bits  = 0
        while(index):
            if index & 1:
                set_bits+=1
            index>>=1
        return chr(set_bits + 97)