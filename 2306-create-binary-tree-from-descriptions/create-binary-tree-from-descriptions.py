
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # note all the values are  unique 


        #keeps all the info of nodes  in the tree , val>address
        nodes = defaultdict()
        #if already we know a node is childe somewhere, then it can't be final root, 
        # even when it is root in some subtree , whose desctiption comes in future
        cant_root = set() 
        # to keep all valid roots , at end gives final root of tree
        root  = set()
        for r,c,l  in descriptions:
            #1.adding node val and and adress to the nodes dict, if it is a new node
            #2.adding this val to root set , if is valid root 
            if r not in nodes:
                node = TreeNode(r)
                nodes[r] = node
                #we not consider a node as root , if already we know it was a child and therefore cant be a root, from 
                #previous descriptions 
                if r not in cant_root:
                    root.add(r)
            node = nodes[r]
            #creating child node 
            # note that in case this child c is already a entry in the nodes dict 
            #we neeed to use the same node rather than creating  a new one 
            if c in nodes:
                child  =nodes[c]
            else:
                nodes[c] = TreeNode(c)   
            child = nodes[c]

            #adding the child to the node
            if l:
               
                node.left = child
            else:
                node.right  = child 
            #if c was qualified as a root node from prev description , and now we 
            #need to remove it, from considering so 
            if c in root:
                root.remove(c)
            cant_root.add(c)
        #FINAL NODE IN THE ROOT , IS THE FINAL ROOT OF THE TREE 
        root_val  = root.pop()
        return nodes[root_val]


        