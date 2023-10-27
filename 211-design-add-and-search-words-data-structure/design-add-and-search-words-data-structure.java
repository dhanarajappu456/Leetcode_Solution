import java.util.HashMap;

class TrieNode {
    public HashMap<Character, TrieNode> children = new HashMap<>();
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
            node.children.putIfAbsent(c, new TrieNode());
            node = node.children.get(c);
        }
        node.isEndOfWord = true;
    }

    public boolean search(String word) {
        return searchInNode(word, root, 0);
    }

    public boolean searchInNode(String word, TrieNode node, int index) {
        if (index == word.length()) {
            return node.isEndOfWord;
        }

        char ch = word.charAt(index);
        if (ch == '.') {
            for (char key : node.children.keySet()) {
                if (searchInNode(word, node.children.get(key), index + 1)) {
                    return true;
                }
            }
            return false;
        } else {
            if (!node.children.containsKey(ch)) {
                return false;
            }
            return searchInNode(word, node.children.get(ch), index + 1);
        }
    }

    public static void main(String[] args) {
        WordDictionary obj = new WordDictionary();
        obj.addWord("word");
        boolean result = obj.search("wo.d");
        System.out.println(result); // should print true
    }
}
