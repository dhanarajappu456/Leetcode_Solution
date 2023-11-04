
from collections import deque as dq , defaultdict as dict
'''
bitmasking solution - always remember this pattern ,when you need to make decisions on the set of elements 
when the constsraints are very low number, you can use bit masking
'''
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        
        '''
        preprocessing , - 
        1)remove duplicate stickers
        2)remove all the stickers that aint give any char in target 
        '''

        #remove duplicate stickers
        stickers  = set(stickers)
        stickerNew  = []

        #only consider stickers having atleast one character in the target
        for stick in stickers: 
            present = False
            for c in stick : 
                if c in target:
                    present  = True
                    break
            if present:
                stickerNew.append(stick)

        #new processed stickers list 
        stickers = list(stickerNew)
        #maks denoting which are the postion in the target that is needed to be obtained, 
        #initiallly all chars is needed so all ones 
        n = len(target)
        mask = (1<<n)-1 

        #characters in the target that need to be sufficed, mapped to list of thier indices,
        #this is needed to know which position in the target  is sufficed currently , 
        #and therfore  unset the mask position , denoting it is sufficed,
        charInd = dict(dq)
        for i,c in enumerate(target):
            charInd[c].append(i)
        
        #call the recursive function for the remaining set of chars,(denoted by the mask)
        @lru_cache(None)
        def rec(mask):
       
            if mask ==0: 
                return 0 
            #try all sticker if it can suffice any remaining character in the target 
            #if yes, call the rec for remaining chars
            old_mask = mask
            ans = float("inf")
            for stick in stickers:
                indices =dict(dq)
                new_mask = mask
                for c in stick:
                    if charInd[c]:
                        indices[c].append(charInd[c][0])
                        ind = charInd[c].popleft()
                        new_mask = new_mask & ~(1<<ind)
                #call recursion if atleast one character can be sufficed, by the sticker
                if indices:
                    ans = min(ans, 1+ rec(new_mask)) 

                #backtracking , setting back the charInd , with original values , before the recursion was called
                for c in indices:
                    for ind in indices[c]:
                        charInd[c].appendleft(ind)
            return ans
        ans = rec(mask)
        #if not possibilites of getting the target , then return -1 
        return -1 if ans == float("inf") else ans 

                    
                    
            
                    
            
