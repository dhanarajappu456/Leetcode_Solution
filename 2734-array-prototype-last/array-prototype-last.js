/**
 * @return {null|boolean|number|string|Array|Object}
 */
//  1)if you call like this ->Array.prototype.last()  
//   "this " refer to the Array.prototype object

//2.if u call like this -> arr = [12,4]
//arr.last() , "this" refer to the current array object

Array.prototype.last = function() {
    console.log("hai",this)
    return this.length  === 0 ? -1 : this[this.length-1]
};

/**
 * const arr = [1, 2, 3];
 * arr.last(); // 3
 */