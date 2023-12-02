<h2>game-of-life Notes</h2><hr>solution using 4 states 

the msb bit represent the new val and the next bit represent prev val  in the cell

00 - initially 0 , and new also 0  
10 initally 0 and new is 1
11  initially 1 and new is 1 
01    initally 1 and new is 0 


so check condition accordingly 

finally change the values of the board based on this state value
