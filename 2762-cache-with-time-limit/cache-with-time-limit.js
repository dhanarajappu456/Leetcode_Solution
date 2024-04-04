var TimeLimitedCache = function() {

    this.timeMap = new Map();
    this.keyVal  =new Map();
    
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    //clear any prev time scheduled on this key 
    const ans   = this.timeMap.has(key)?true: false
    clearTimeout(this.timeMap.get(key))
    //update the key with new val
    this.keyVal.set(key, value)
    //schedule to delete the key after "duration"
    //which deletes the key from KeyValmap and also timer info od key from the timeMap
    const id  = setTimeout(()=>{this.keyVal.delete(key)
    this.timeMap.delete(id)},duration)
    //update the timeMap with new timer id of the key, so that in can be cancelled ,
    //if same key updated before it being executed
    this.timeMap.set(key, id) 
    return ans
    
    
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    
    return this.keyVal.get(key) || -1
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    return this.keyVal.size
};

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */