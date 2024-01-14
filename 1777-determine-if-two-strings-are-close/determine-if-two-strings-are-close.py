class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        mp1 = {}
        mp2  ={}

        freq1 =  []
        freq2= []


        for  c in word1:
            mp1[c] = mp1.get(c,0)+1
        
        for  c in word2:
            mp2[c] = mp2.get(c,0)+1
        for c in mp1:
            freq1.append(mp1[c])
        for c in mp2:
            freq2.append(mp2[c])
        freq1.sort()
        freq2.sort()
        return freq1 == freq2  and mp1.keys() == mp2.keys()
