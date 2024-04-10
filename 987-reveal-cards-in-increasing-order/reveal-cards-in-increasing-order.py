class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        #solution 1 - simulation - with 2 pointer

        #idea is we put the number in deck 
        #to spot  in result , in the order the numbers 
        #from res are  accessed , as mentioned in game
        
        #one pointer result 
        #one poiter on deck
        #we simulate the game , 
        #add the current number in deck to the res , and 
        #skip a empty poistion( denoted by -1) adds the next number 
        #in hte deck to this poisiton 
        n  = len(deck)
        deck.sort()
        res =[-1 for i in range(n)]
        i =0
        for ind , num in enumerate(deck):
            res[i]  = num
            #after placing last number  , the task is finished
            #so no need of skipping a empty spot and finding next empty spot 
            #(as all spots are filled)
            if ind<n-1:
                #finding first empty space
                while(res[i]!=-1):
                    i = (i+1)%n
                #skipping first empty space
                i =(i+1)%n
                #finding next empty space
                while(res[i]!=-1):
                    i = (i+1)%n
        return res

        #t nlogn(sort) + n^2( assuming worst of inner loop when there are many non tmpty values filled
        #adjcent)
        #s 1( res not considered)
        
            

            
            




        