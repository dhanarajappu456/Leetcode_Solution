/**
 * @param {string} s
 * @return {number}
 */
var maxScore = function(s) {
     let totOnes = s.split('1').length - 1;
        let score = 0;
        let lZero = 0, lOne = 0;
        const n = s.length;

        for (let i = 0; i < n - 1; i++) {
            if (s[i] === '0') {
                lZero++;
            } else {
                lOne++;
            }

            const rOne = totOnes - lOne;
            score = Math.max(score, lZero + rOne);
        }

        return score;
};