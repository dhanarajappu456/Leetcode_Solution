class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        #solution 1  - simulation
        students = deque(students)
        i=0
        while(sandwiches and students):

            tries =0 
          
            #we need to try removing from frontof queue and ut at end of it 
            # if top of stack cant be consumed by current student
            while(tries<len(students) and students[0]!=sandwiches[i]):
                tries+=1
                students.append(students.popleft())
            #this means without removing and adding all the students
            #the loop ended, means we have a match , in which case consume top stack
            
            if tries<len(students):
                students.popleft()
                #updating the index of sandwich , to next sandwich
                i+=1
            
            #tried all students , no match so return remaining number of students
            else:
                
                return len(students)
            
        return 0 



        