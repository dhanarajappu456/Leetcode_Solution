
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:


        nodes = defaultdict()
        cant_root = set() 
        root  = set()
        for r,c,l  in descriptions:

            if r not in nodes:
                node = TreeNode(r)
                nodes[r] = node
                if r not in cant_root:
                    root.add(r)
            node = nodes[r]


            if c in nodes:
                child  =nodes[c]
            else:
                nodes[c] = TreeNode(c)   
            child = nodes[c]
            if l:
               
                node.left = child
            else:
                node.right  = child 

            if c in root:
                root.remove(c)
            cant_root.add(c)

        root_val  = root.pop()
        return nodes[root_val]


        