class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        i = 0
        j = 0 
        m,n = len(players) , len(trainers)
        count = 0 
        while(i <m and j<n):

            if players[i] > trainers[j]:
                j+=1 
            else:
                i+=1
                j+=1
                count +=1
        return count


