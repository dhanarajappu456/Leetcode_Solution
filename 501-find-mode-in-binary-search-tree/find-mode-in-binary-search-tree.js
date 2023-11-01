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
var findMode = function(root) {
 
    var ans = [];
    var count = 0;
    var max = 0;
    var prev = 10 ** 5 + 1;

    var rec = function(node) {
        if (node === null) {
            return;
        }

        rec(node.left);

        if (node.val === prev) {
            count++;
        } else {
            count = 1;
        }

        if (count === max) {
            ans.push(node.val);
        } else if (count > max) {
            ans = [node.val];
            max = count;
        }

        prev = node.val;

        rec(node.right);
    };

    rec(root);
    return ans;
};
