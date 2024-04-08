class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        #solution 1  - simulation
        stud_0, stud_1 = students.count(0), students.count(1)
        stud_cnt = [stud_0, stud_1]
       
        i=0
        while(i<len(sandwiches)):
          
            if stud_cnt[sandwiches[i]] ==0:
                return sum(stud_cnt)
            stud_cnt[sandwiches[i]]-=1    
            i+=1
        
        return 0 



        