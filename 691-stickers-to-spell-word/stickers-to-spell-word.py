from collections import defaultdict as dict

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:

        charInd = dict(list)
        #store the character mapped to the indices 
        for i,c in enumerate(target):
            charInd[c].append(i)
        n = len(target)
        mask = (1<<n)-1 
        #call the recursive function for the remaining set of chars,(denoted by the mask)


        @lru_cache(None)
        def rec(mask):
            #print(bin(mask))
            if mask ==0: 
                return 0 
            
            #try all sticker if it can suffice any remaining character in the target 
            #if yes, call the rec for remaining chars
            old_mask = mask
            
            ans = float("inf")
            for stick in stickers:
                indices =dict(list)
                new_mask = mask
                for c in stick:
                    if charInd[c]:
                        indices[c].append(charInd[c][0])
                        ind = charInd[c].pop(0)
                        new_mask = new_mask & ~(1<<ind)
                        
                if indices:
                    ans = min(ans, 1+ rec(new_mask)) 

                for c in indices:
                    for ind in indices[c]:
                        charInd[c].insert(0,ind)
            return ans
        ans = rec(mask)
        return -1 if ans == float("inf") else ans 

                    
                    
            
                    
            
