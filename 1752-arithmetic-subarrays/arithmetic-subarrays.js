/**
 * @param {number[]} nums
 * @param {number[]} l
 * @param {number[]} r
 * @return {boolean[]}
 */
var checkArithmeticSubarrays = function(nums, l, r) {
     const n = nums.length;
        const m = l.length;
        const res = [];

        for (let i = 0; i < m; i++) {
            const a = l[i];
            const b = r[i];

            const arr = nums.slice(a, b + 1);

            arr.sort((x, y) => x - y);
            const diff = arr[1] - arr[0];
            let j = 2;

            while (j < arr.length) {
                if (arr[j] - arr[j - 1] !== diff) {
                    res.push(false);
                    break;
                }
                j++;
            }

            if (j === arr.length) {
                res.push(true);
            }
        }

        return res;
};


