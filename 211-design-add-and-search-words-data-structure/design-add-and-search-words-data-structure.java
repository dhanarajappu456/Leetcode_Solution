class TrieNode {
    public TrieNode[] children = new TrieNode[26]; // assuming all lowercase letters
    public boolean isEndOfWord = false;
}

public class WordDictionary {
    private TrieNode root;

    public WordDictionary() {
        root = new TrieNode();
    }

    public void addWord(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            if (node.children[c - 'a'] == null) {
                node.children[c - 'a'] = new TrieNode();
            }
            node = node.children[c - 'a'];
        }
        node.isEndOfWord = true;
    }

    public boolean search(String word) {
        return searchInNode(word, root);
    }

    public boolean searchInNode(String word, TrieNode node) {
        for (int i = 0; i < word.length(); i++) {
            char ch = word.charAt(i);
            if (ch == '.') {
                for (int j = 0; j < 26; j++) {
                    if (node.children[j] != null && searchInNode(word.substring(i + 1), node.children[j])) {
                        return true;
                    }
                }
                return false;
            } else {
                if (node.children[ch - 'a'] == null) {
                    return false;
                }
                node = node.children[ch - 'a'];
            }
        }
        return node.isEndOfWord;
    }

    public static void main(String[] args) {
        WordDictionary obj = new WordDictionary();
        obj.addWord("word");
        boolean result = obj.search("wo.d");
        System.out.println(result); // should print true
    }
}
