var sortVowels = function(s) {
    var vowelSet = new Set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']);
    var vowList = [];

    for (var i = 0; i < s.length; i++) {
        var c = s[i];
        if (vowelSet.has(c)) {
            vowList.push(c);
        }
    }

    vowList.sort();

    var res = [];
    var v = 0;
    for (var i = 0; i < s.length; i++) {
        var char = "";
        var c = s[i];
        if (!vowelSet.has(c)) {
            char = c;
        } else {
            char = vowList[v];
            v++;
        }
        res.push(char);
    }

    return res.join("");
};

