class Solution:
    def isPathCrossing(self, path: str) -> bool:

        curr_x,curr_y =0,0
        s = set()
        s.add((0,0))
        for d in path:
            if d == "N":
                curr_x , curr_y = curr_x, curr_y+1
            if d == "E":
                curr_x,curr_y = curr_x+1, curr_y
            if d == "W":
                curr_x,curr_y = curr_x-1, curr_y
            if d =="S":
                curr_x,curr_y = curr_x, curr_y-1

            if (curr_x,curr_y) in s:
                return True
            s.add((curr_x,curr_y))
        
        return False
        