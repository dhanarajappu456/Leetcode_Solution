/**
 * @param {number[]} nums
 * @return {number}
 */
var maxScore = function(nums) {
     const n = nums.length;
        const mask = (1 << n) - 1;
        const memo = new Map();


        
        function gcd(a, b) {
            return b === 0 ? a : gcd(b, a % b);
        }

        function rec(i, mask) {
            if (mask === 0) {
                return 0;
            }
            if (memo.has(`${i}-${mask}`)) {
                return memo.get(`${i}-${mask}`);
            }

            let ans = 0;
            for (let j = 0; j < n - 1; j++) {
                if ((1 << (n - 1 - j)) & mask) {
                    for (let k = j + 1; k < n; k++) {
                        if ((1 << (n - 1 - k)) & mask) {
                            let newMask = mask & ~(1 << (n - 1 - j));
                            newMask = newMask & ~(1 << (n - 1 - k));
                            ans = Math.max(ans, i * gcd(nums[j], nums[k]) + rec(i + 1, newMask));
                        }
                    }
                }
            }

            memo.set(`${i}-${mask}`, ans);
            return ans;
        }

        return rec(1, mask);
};



