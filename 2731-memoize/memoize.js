/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    let mp  = new Map()

    return function(...args) {

        const s = args.toString();

        if( mp.has(s) ){
            return mp.get(s)
        }
        else{
            const res = fn(...args)
            mp.set(s,res)
            return res 

        }
            
            
        
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */