'''

1)approach1 - construct the grapah from wordlist, with key as each word

remember the length of each word in wordlist == length of startword == length of endword
create the graph ,where each node is neighbours to each other, if they diff in only 1 char 
run the bfs on them to find shortest number of transformation to reach endword


t create adj list (n^2*m ) + bfs (v+e = n+ n^2)
s (v+e = n + n^2)

2)approach2 

same logic as first but creating graph with key as the pattern , we create a pattern
eg: *ot  which maps , all words that is of this from , meaning it has any character at first place , but, 
"ot" after that

then do bfs using this adj list, 
doing this way , reduce, the time complexity 
from n^2m to nm^2



t create adj list (n*m^2 ) + bfs (v+e = n+ n^2)
s (v+e = n + n^2)



'''

#approach 2 

from collections import defaultdict as dict, deque as dq
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #if the endword not in  wordlist then for sure , we cant make it to end wor 
        if endWord not in wordList :
            return 0
        adj = dict(list)
        visited  = set()
        #creating adjlist with pattern as key , is more efficient than creating asjlist directly 
        #here time complexity  = n*m^2
        for word in wordList:#n
            
            for ind in range(len(word)): #m
                pattern  = word[:ind] + "*" +word[ind+1:]  #m 
                adj[pattern].append(word)
        
        q= dq([(beginWord,1)])
        visited.add(beginWord)
        while(q): #(v=e = n+n^2)
            
            word,step =q.popleft()
            for ind in range(len(word)):
                pattern = word[:ind] + "*" +word[ind+1:]
                #this line of adding pattern as visited, is not necessary, but for better runtime ,#optimisation
                #that , if the  same pattern is occuring again , there is no need to visit any word belonging 
                #to that pattern,since it has been already visited, which  would give  the sortest path if it #present via this pattern

                if pattern not in visited:
                    visited.add(pattern)
                    for neib in adj[pattern]:
                            
                            if neib ==endWord:
                                return step+1
                            if neib not in visited:
                                q.append((neib,step+1))
                                visited.add(neib)
                
                        
                            
        return 0