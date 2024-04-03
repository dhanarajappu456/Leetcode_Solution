/**
 * @param {number[]} nums
 * @return {void}
 */
var ArrayWrapper = function(arr) {
    this.arr = arr
};

/**
 * @return {number}
 */
ArrayWrapper.prototype.valueOf = function() {
    return this.arr.reduce((acc,val)=>acc+val,0)
   
}

/**
 * @return {string}
 */
ArrayWrapper.prototype.toString = function() {
    //console.log(this.arr)
    return JSON.stringify(this.arr)
 
}

/**
 * const obj1 = new ArrayWrapper([1,2]);
 * const obj2 = new ArrayWrapper([3,4]);
 * obj1 + obj2; // 10
 * String(obj1); // "[1,2]"
 * String(obj2); // "[3,4]"
 */