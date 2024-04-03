/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
var debounce = function(fn, t) {
    let id; 
    return function(...args) {
        //if current function call is before execution of previous function call which was scheduled
        //in another word there is no atleast a gap of time b/w two successive calls , cancel previous 
        //scheduled call , and schedule current call to be executed after t 
        clearTimeout(id)
        id  = setTimeout(()=>fn(...args),t)
    }
};

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */