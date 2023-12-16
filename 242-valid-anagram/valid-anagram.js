/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    

        if (s.length != t.length){
            return false
        }
        chars  = Array(26).fill(0)

      
        for(let c of s){

            chars[c.charCodeAt(0)-'a'.charCodeAt(0)]+=1
            
        }
        
        for(let c of t){

            chars[c.charCodeAt(0)-'a'.charCodeAt(0)]-=1
            if (chars[c.charCodeAt(0)-'a'.charCodeAt(0)] <0 ){
                console.log(chars) 
                return false
            }
            
        }
        return true
                    

            
           
            
      
};