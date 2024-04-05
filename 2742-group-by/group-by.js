/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    const map = {};
    this.forEach((val)=>{

        const id = fn(val);
        if (!(id in map))
            map[id] = []
        map[id].push(val)
        
    })

    return map;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */