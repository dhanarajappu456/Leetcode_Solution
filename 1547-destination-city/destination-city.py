'''
#solution 1 - hashmp - using out degreee - 2 pass 
1 pass to create outdegree map , second pass for checking if a dest dont have the outdegree 

t  2n 
s  n

#solution 2 - using hashset - 2pass

add all sources to the hashset then 
iterate again on the paths to get all destination , and see if any dest not in source, which is the ans

t 2n
s n 



#solution 3 - using 2 hashset - 1-pass

we keep one set for keeping all source visited so far and another set for possible_dest 

as we iterate on the paths, we add source  to the source set and also remove this node from possible_dest  , in case it was added as dest previously 

also update the possible_dest with the new dest in case it was not a source previously 

at the end our possible_set would contain only single value which is the ans 

t 2n
s n



store a  map where outdegree for each source is marked as 1 or 0 

at th end iterate on all destination and check if outdegree of it is ==0 which is  the ans
'''

#solution 3
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        mp  = {}
        ans  =""
        possible_dest =set()
        sources =set()
        for s,d in paths:
            #in case the s was dest so far remove it from the set 

            if s in possible_dest:
                possible_dest.remove(s)
            # update the sources
            sources.add(s)
            # update possible_dest
            if d not in sources:
                possible_dest.add(d)

        return possible_dest.pop()
        