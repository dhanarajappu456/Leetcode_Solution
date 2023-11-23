/**
 * @param {string} s
 * @return {string[]}
 */
var restoreIpAddresses = function(s) {
    
    let res = [];

    function rec(i, ans, partition) {
        if (partition === 4) {
            if (i === s.length) {
                res.push(ans.join('.'));
            }
            return;
        }

        for (let j = i; j < Math.min(i + 3, s.length); j++) {
            let sub = s.substring(i, j + 1);
            let val = parseInt(sub);

            if (val <= 255 && !(j !== i && s[i] === '0')) {
                ans.push(sub);
                rec(j + 1, ans, partition + 1);
                ans.pop();
            } else {
                break;
            }
        }
    }

    rec(0, [], 0);
    return res;
};

