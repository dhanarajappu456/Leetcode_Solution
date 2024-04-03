/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {

    let res= []

    let i =0
    const n = arr.length
    while(i<n){
        res.push(arr.slice(i,i+size))   
        i+=size
    }
        
    return res


    
};
