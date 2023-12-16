/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    

    const sMap  = new Map()
    const tMap =   new Map()


    for(const c of s){
        sMap.set(c, (sMap.get(c)||0 )+ 1 )

    }

    for(const c of t){
        tMap.set(c, (tMap.get(c)||0 )+ 1 )

    }
    if (tMap.size !== sMap.size){
        return false
    }
        
    for ([key, val] of sMap){

            if (!tMap.has(key) || tMap.get(key)!== sMap.get(key)){
                return false;

            }

    }

    return  true

};