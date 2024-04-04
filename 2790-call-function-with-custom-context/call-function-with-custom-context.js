/**
 * @param {Object} context
 * @param {Array} args
 * @return {null|boolean|number|string|Array|Object}
 */
//Function.prototype is prototype of all the function object
//hence of all the custom function object like increment given in eg :
// the polyfill call the custom function with the custom context , which is the first argument 
//argument passed to it and , rest argument passed as rest arrguments to the custom function being called




/* 

functions to change context in js 
__________________________________________

1) call  - to call a function with custom context
fn.call(context_obj, arg1,arg2,...)
where arg1, arg2 are args to fn 
2) bind - return a object  with passed context which can be called with different arguments of choice
fn.bind(context_object)(arg1, arg2, ...)
3)apply - like the call but takes args as array

fn.apply(context_obj,[arg1,arg2,...]) 

eg:function a(a1,a2){
    
    console.log(this,a1,a2) 
}
a.call({1:8},90,100)  //{ '1': 8 } 90 100
a.bind({1:8})(90,100)  //{ '1': 8 } 90 100
a.apply({1:8},[90,100])  //{ '1': 8 } 90 100
 

*/
Function.prototype.callPolyfill = function(context, ...args) {
    return  this.call(context,...args)
}

/**
 * function increment() { this.count++; return this.count; }
 * increment.callPolyfill({count: 1}); // 2
 */