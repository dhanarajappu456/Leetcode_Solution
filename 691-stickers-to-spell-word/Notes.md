<h2>stickers-to-spell-word Notes</h2><hr>bit mask solution , 

mask is of length of target, 
1's in the mask denote the position in the target, the character at which we need 

the state rec(mask) denote min number of stickers needed to collect characters represented by the mask 

t  n*m * ( 2^k  ) -> n =len of stickers,  m - len of each sticker and k is the length of target 
s 2^k(memo dict space)  + stack(k)
