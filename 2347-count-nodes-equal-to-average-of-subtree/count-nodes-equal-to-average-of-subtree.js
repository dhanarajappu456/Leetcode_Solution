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
 * @return {number}
 */
var averageOfSubtree = function(root) {

    let ans = 0;

        function rec(node) {
            if (node === null) {
                return [0, 0];
            }
            const [leftSum, leftCount] = rec(node.left);
            const [rightSum, rightCount] = rec(node.right);
            if (Math.floor((leftSum + rightSum + node.val) / (leftCount + rightCount + 1)) === node.val) {
                ans++;
            }
            return [leftSum + rightSum + node.val, leftCount + rightCount + 1];
        }

        rec(root);
        return ans;
    
};