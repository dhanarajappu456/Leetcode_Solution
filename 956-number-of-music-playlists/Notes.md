<h2>number-of-music-playlists Notes</h2><hr>memo code 

at any  point we can have 2 choices, either choose the unqiue song , or already chosen song.

a) when calculating the  number of playlist , when we can choose a unique song ,then number of remaining unique song  = n - number  unique song already chosen , then for each of the song we call the recursion , with totsongchosen + 1, and totuniquesongchosen + 1


b)when calulating the number of playlist , when we can repeat a song already chosen , 

repetable song = number of unique song chosen - k, so for each of them we call the recursion with totsong+1


note that : 
the state (totChosen, totUniqueChosen) indicate the tot possible playlist , with totchosen number of songs chosen in total and totuniqueChosen , 