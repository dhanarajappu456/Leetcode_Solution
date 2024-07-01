<h2>count-numbers-with-unique-digits Notes</h2><hr>using permutation 

when given say n=  3  

we find count of unique single diigit number 
then unique 2 digit , then unique 4  digiy number and sum it all

t= n^2
s 1 


note we cant directly say count = 10*9*8, 

as that doint consider case like 001,002,003,....009

and 010, 020 , 030, ...   090, which is valid , therefore we need to take cases seperately , starting from unqiue , single digit, uniqe 2 digit, unique 3 digit .