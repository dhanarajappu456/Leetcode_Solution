
function Node(){

    this.dic = { };
    this.isEnd = false;
}


var WordDictionary = function() {

        this.head = new Node()
        
    
};

/** 
 * @param {string} word
 * @return {void}
 */
WordDictionary.prototype.addWord = function(word) {

    let temp = this.head;
    

    for (let c of word) {
            if (!(c in temp.dic)) {
                temp.dic[c] = new Node();
            }
            temp = temp.dic[c];
        }
    temp.isEnd = true;
};

/** 
 * @param {string} word
 * @return {boolean}
 */
WordDictionary.prototype.search = function(word) {
    let n = word.length;
   

    let dfs = (node, ind) =>{
        if (ind === n) {
            return node.isEnd;
        }
        let ch = word[ind];
        if (ch === ".") {
            for (let c in node.dic) {
                if (dfs(node.dic[c], ind + 1)) {
                    return true;
                }
            }
            return false;
        } else {
            if (!(ch in node.dic)) {
                return false;
            }
            return dfs(node.dic[ch], ind + 1);
        }
    }

    return dfs(this.head, 0);
};

/** 
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = new WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */