/**
 * @param {number[]} nums
 * @return {number}
 */
var maxCoins = function(nums) {
  function rec(i, j) {
        if (i > j) {
          return 0;
        }

      if (memo[i][j] !== -1) {
        return memo[i][j];
      }

    let maxCoins = 0;
    for (let p = i; p <= j; p++) {
     
      maxCoins = Math.max(
        maxCoins,
        nums[i - 1] * nums[p] * nums[j + 1] + rec(i, p - 1) + rec(p + 1, j)
      );
    }
    
    memo[i][j] = maxCoins;
    return maxCoins;
  }
  nums = [1, ...nums, 1];
  const n = nums.length;

  const m = n-1;

 const memo = Array.from({ length: m }, () =>  Array(m).fill(-1));

  
  
  ans = rec(1, m-1);
 
  return ans

};

// function maxCoins(nums) {
//   const n = nums.length;
//   const memo = new Array(n + 2).fill(null).map(() => new Array(n + 2).fill(0));

  

// const nums = [3, 1, 5, 8];
// console.log(maxCoins(nums));
