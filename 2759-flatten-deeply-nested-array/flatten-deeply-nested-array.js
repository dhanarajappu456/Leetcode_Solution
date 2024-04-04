/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */

/*
recursion - 
if current depth is <=n 
    if current element is number just append to res
    if current element is array , we need to further rec calls 
else
    just append the current array to res

 */
var flat = function (arr, n) {


    const res   = [];

    function rec(arr, depth){
        
        if(depth<=n){

            for(const item of arr){
                //call recursion for the array
                if (item instanceof Array)
                    rec(item,depth+1);    
                //append the element to res
                else
                    res.push(item);
            
            } 
        }
        // just push current array to res
        else
            res.push(arr);
       
        
    }
    rec(arr,0)
    return res
    


};