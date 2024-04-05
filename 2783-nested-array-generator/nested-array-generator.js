/**
 * @param {Array} arr
 * @return {Generator}
 */
 /*
 yield returns one value at a time 

 but , to yield one value at a time from list , iterable , another generator, from within a 
 generator , then  we need to use yield*
 
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