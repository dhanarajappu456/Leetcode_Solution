/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {


    const res   = [];

    function rec(arr, depth){
        
        if(depth<=n){

            for(const item of arr){
                  
                if (item instanceof Array)
                    rec(item,depth+1);    
                else
                    res.push(item);
            
            } 
        }
        else
            res.push(arr);
       
        
    }
    rec(arr,0)
    return res
    


};