"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

'''
do a dfs, if the node visited is note visited before create new node for the value, and keep it  in a dict
with val->newNode address, 
if it is already visited , just return that newlycreated that has  been created so far node for the values 
'''

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        newNodes= {}
        def rec(node):

            if node ==None:
                return None
            if node.val in newNodes: 
                return newNodes[node.val]


            newNode  =Node(node.val)
            newNodes[node.val] = newNode


            for neib in node.neighbors:
                newNeib = rec(neib)
                newNode.neighbors.append(newNeib)
            

            return newNode
        

        return rec(node)

        '''
        t n
        s n(map)+aux(n)

        '''