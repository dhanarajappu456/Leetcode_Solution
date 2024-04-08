#for this problem the sandwich stack given is reveresed stack , 
#that is top is on left , not on right
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        #solution 2 using variable
        #keep track of cnt of students consuming each type
        #now we kinda simulate the solution1 
        #such that , we take top of sandwich stack denoted by ith variable,
        #check if we can consume it ( possible iff there is atlest one student of that type, else ,cant so return
        #remainnig number of students)
        #if possible eat we decrement cnt of that type of students

        #eg test , students  = [1,1,1]
        #sandwich = [0,1,1] 
        #ans =3 (as no students of type 0, is remaining, if at all we can try deq and enq them so that 
        #they match the top of stack)

        stud_0, stud_1 = students.count(0), students.count(1)
        stud_cnt = [stud_0, stud_1]
       
        i=0
        while(i<len(sandwiches)):
            #if we cant consume curretn item in the sandwich stack(ie, no such type pf student remaining =)
            #return the rem number of students
       
            if stud_cnt[sandwiches[i]] ==0:
                return sum(stud_cnt)
            # student of type of current item takes the current item
            
            stud_cnt[sandwiches[i]]-=1   
            #assumption of pop 
            i+=1
        
        return 0 



        