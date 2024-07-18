<h2>number-of-good-leaf-nodes-pairs Notes</h2><hr>solution 1  - DFS

Essentially we will  have the left and right list for a node , which stores the depths to all the leaf nodes , and once we  have this information , we check differnt pair of depths by combinining the pair from  this left and right list , whether they make d <= distance


t n  * n^2 = n^3 
s  n