<h2>shortest-subarray-with-or-at-least-k-ii Notes</h2><hr>sliding window - like the smallest subarray with the sum>=k


but when contracting the left side ,we need to have keps a  bits array 
that indicate all the counts of 1 for each  of the 32 bits position 
so that when we remove the nums from subarray from left or when we add the nums to right , this bits array keeps the count and update it accordingly 


t n
s o(1) = 32

