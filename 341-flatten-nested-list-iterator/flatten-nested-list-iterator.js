/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * function NestedInteger() {
 *
 *     Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     @return {boolean}
 *     this.isInteger = function() {
 *         ...
 *     };
 *
 *     Return the single integer that this NestedInteger holds, if it holds a single integer
 *     Return null if this NestedInteger holds a nested list
 *     @return {integer}
 *     this.getInteger = function() {
 *         ...
 *     };
 *
 *     Return the nested list that this NestedInteger holds, if it holds a nested list
 *     Return null if this NestedInteger holds a single integer
 *     @return {NestedInteger[]}
 *     this.getList = function() {
 *         ...
 *     };
 * };
 */
/**
 * @constructor
 * @param {NestedInteger[]} nestedList
 */
var NestedIterator = function(nestedList) {





        this.list  = [];
        this.p = 0;
        // remember to use arrow function here,  since inside arrow function get refernced to the this of enclosing context

        // but if we has  normal function here ,  this would be referred to window object , or undefined , if you want to sue function itself, then you have to explicitly bind the context of this of  rec function to the outer object
        function rec(item){

            
            if( item.getInteger()!==null){
                
                this.list.push(item.getInteger());
                return;


            }

            for(let it of item.getList() ){

                bound(it);
            }
            

        }
        //binding this of rec to outer  object , and creating a new function called bound
        let bound = rec.bind(this)
        for (let item of  nestedList){


            bound(item);
        }
     
    
};


/**
 * @this NestedIterator
 * @returns {boolean}
 */
NestedIterator.prototype.hasNext = function() {
    

 return this.p<this.list.length

};

/**
 * @this NestedIterator
 * @returns {integer}
 */
NestedIterator.prototype.next = function() {
   
    return( this.list[this.p++])
};

/**
 * Your NestedIterator will be called like this:
 * var i = new NestedIterator(nestedList), a = [];
 * while (i.hasNext()) a.push(i.next());
*/