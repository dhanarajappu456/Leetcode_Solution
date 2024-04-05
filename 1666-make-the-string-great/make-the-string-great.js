/**
 * @param {string} s
 * @return {string}
 */
var makeGood = function(s) {
    const stack = [];
        
        for (const c of s) {
            if (stack.length && (stack[stack.length - 1].charCodeAt(0) + 32 === c.charCodeAt(0) || stack[stack.length - 1].charCodeAt(0) - 32 === c.charCodeAt(0))) {
                stack.pop();
            } else {
                stack.push(c);
            }
        }
        
        return stack.join('');
};