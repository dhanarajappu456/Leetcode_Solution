/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var largestValues = function(root) {

    ans = []
    q= [ ]
    if( root != null){

        q.push(root)

    }

    let max_val = -Infinity
    
    while(q.length){

        const len  = q.length
        let max_val = -Infinity
        for (let i = 0; i < len; i++) {

            const node = q.shift()
            max_val = Math.max(max_val, node.val)
            
            
            if (node.left)
          
                q.push(node.left)
            if ( node.right)
              
                q.push(node.right)

        } 
        ans.push(max_val)
           
               
        


    }
    return ans

        

    
};