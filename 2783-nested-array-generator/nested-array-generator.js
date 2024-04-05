/**
 * @param {Array} arr
 * @return {Generator}
 */
var inorderTraversal = function*(arr) {
     const res   = [];
 
    function* rec(arr){

            console.log("hai")
            for(const item of arr){
                //call recursion for the array
                if (item instanceof Array)
                    yield* rec(item);    
                //append the element to res
                else
                    yield item
            
            } 
  
        
       
        
    }
    yield* rec(arr)
  
};

/**
 * const gen = inorderTraversal([1, [2, 3]]);
 * gen.next().value; // 1
 * gen.next().value; // 2
 * gen.next().value; // 3
 */