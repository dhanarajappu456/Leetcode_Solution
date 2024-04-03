/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function(fn, t) {
    return async function(...args) {
        return new Promise(async(resolve,reject)=>{
        // this is used to reject the promise if the allowed time t is reached to resolve the fn
        // this is scheduled to execute after t second , during which time is added to 
        //event queue for executing 
        const timeOutId  = setTimeout(()=> reject("Time Limit Exceeded"),t)
        try{
            
            const data = await fn(...args)
             
                resolve(data)
                //since the fn resolved within the time t , we no more need to execute tht 
                //scheduled reject so canceel it , to avoid unnecessary memory leaks
                clearTimeout(timeOutId)
        }

        catch(err){
            // the function could some time throw the errors , in which case is to be rejected 
            //eg:async () => { throw "Error"; }
            reject(err)
            clearTimeout(timeOutId)
        }

        })
        
    }
};

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */